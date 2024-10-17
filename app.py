import PyPDF2

def save_first_three_pages(input_pdf, output_pdf):
    # Open the input PDF file
    with open(input_pdf, 'rb') as infile:
        # Initialize PDF reader
        reader = PyPDF2.PdfReader(infile)
        
        # Create a PDF writer object
        writer = PyPDF2.PdfWriter()

        # Check if the document has at least 3 pages
        num_pages = min(3, len(reader.pages))

        # Add first 3 pages to the writer
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            writer.add_page(page)

        # Write the first 3 pages to the output PDF
        with open(output_pdf, 'wb') as outfile:
            writer.write(outfile)
    
    print(f"Saved first {num_pages} pages to {output_pdf}")

# Example usage
input_pdf = 'input_document.pdf'
output_pdf = 'first_3_pages.pdf'
save_first_three_pages(input_pdf, output_pdf)