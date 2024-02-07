from docx import Document
from docx.oxml.ns import qn

def get_default_run_font_properties(docx_file):
    # Load the document
    document = Document(docx_file)
    
    # Access the document styles part
    styles = document.styles.element
    
    # Find the default run style (rPrDefault)
    rPrDefault = styles.find(qn('w:rPrDefault'))
    if rPrDefault is None:
        return None  # Default run properties not found
    
    # Extract font name and size from the default run properties
    default_font_name = None
    default_font_size = None
    
    rPr = rPrDefault.find(qn('w:rPr'))
    if rPr is not None:
        rFonts = rPr.find(qn('w:rFonts'))
        sz = rPr.find(qn('w:sz'))
        
        if rFonts is not None:
            default_font_name = rFonts.get(qn('w:ascii'))  # Use 'w:ascii' as a proxy for the font name
            
        if sz is not None:
            default_font_size = sz.get(qn('w:val'))  # Font size in half-points

    return default_font_name, default_font_size

# Replace 'your_document.docx' with the path to your document
default_font_name, default_font_size = get_default_run_font_properties('your_document.docx')
print(f"Default Font Name: {default_font_name}, Default Font Size: {default_font_size} (in half-points)")
