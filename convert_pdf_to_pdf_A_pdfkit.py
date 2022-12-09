import pdfkit

#Set the input and output file paths
input_file = "input.pdf"
output_file = "output.pdf"

#METHOD 1
pdf = pdfkit.PDFKit()
pdf.to_pdfa(input_file, output_file.pdf)

#METHOD 2
#set the PDF/A options
pdfa_options = {
    "PDFA": True,
    "PDFACompatibilityPolicy": "1b"
}
#Convert the PDF to PDF/A using pdfkit
pdfkit.from_file(input_file, output_file, options=pdfa_options)
