import pypdf2

# Open the PDF file
with open('my_file.pdf', 'rb') as f:
    pdf = pypdf2.PdfFileReader(f)

# Check if the PDF is a PDF A/3 document
if pdf.getXmpMetadata() is not None:
    xmp = pdf.getXmpMetadata()
    if xmp.get('pdfaid:conformance') == 'PDF/A-3B':
        print('This is a PDF A/3 compliant document!')
    else:
        print('This is not a PDF A/3 compliant document')
else:
    print('This is not a PDF A/3 compliant document')
