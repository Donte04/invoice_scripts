from PyPDF2 import PdfFileReader, PdfFileWriter

#open the PDF file and read it using the PdfFileReader
pdf_file = open('file.pdf', 'rb')
pdf_reader = PdfFileReader(pdf_file)

#create a new PdfFileWriter and add the pages from the PDF reader
pdf_writer = PdfFileWriter()
for page in pdf_reader.pages:
    pdf_writer.addPage(page)

#add the XML data as an XMP metadata object to the PDF writer
xml_data = b'<xml>data</xml>'
pdf_writer.addMetadata(xml_data)

#save
output_file = open('output.pdf', 'wb')
pdf_writer.writer(output_file)
output_file.close()
