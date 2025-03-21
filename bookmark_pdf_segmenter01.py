import os
from PyPDF2 import PdfReader, PdfWriter

def extract_sections_by_bookmarks(input_pdf, output_dir):
    """
    Extract sections from a PDF based on top-level bookmarks.
    
    Args:
        input_pdf (str): Path to the input PDF file
        output_dir (str): Directory to save the extracted PDF sections
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the PDF
    reader = PdfReader(input_pdf)
    
    # Get the outline (bookmarks)
    outlines = reader.outline
    
    # Filter to get only top-level bookmarks (chapters/main sections)
    top_level_bookmarks = [outline for outline in outlines if not isinstance(outline, list)]
    
    # Process each top-level bookmark
    for i, bookmark in enumerate(top_level_bookmarks):
        # Get the title and target page
        title = bookmark['/Title']
        page_num = reader.get_destination_page_number(bookmark)
        
        # Determine end page (next bookmark or end of document)
        if i < len(top_level_bookmarks) - 1:
            end_page = reader.get_destination_page_number(top_level_bookmarks[i + 1]) - 1
        else:
            end_page = len(reader.pages) - 1
        
        # Create a new PDF with the pages from this section
        writer = PdfWriter()
        for j in range(page_num, end_page + 1):
            writer.add_page(reader.pages[j])
        
        # Clean the title for use as a filename
        clean_title = ''.join(c if c.isalnum() or c in [' ', '-', '_'] else '_' for c in title)
        output_file = os.path.join(output_dir, f"{i+1:02d}_{clean_title}.pdf")
        
        # Save the new PDF
        with open(output_file, 'wb') as out_file:
            writer.write(out_file)
        
        print(f"Created: {output_file} (Pages {page_num+1} to {end_page+1})")

if __name__ == "__main__":
    # Replace with your actual file path
    input_pdf = "Book Title Here.pdf"
    output_dir = "extracted_chapters"
    
    extract_sections_by_bookmarks(input_pdf, output_dir)