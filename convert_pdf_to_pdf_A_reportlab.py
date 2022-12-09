from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Load the font
font_file = "font.ttf"
pdfmetrics.registerFont(TTFont("fontname", font_file))

# Create a canvas object
c = canvas.Canvas("output.pdf", pdf_a=True)

# Set the PDF/A metadata
c.setTitle("My PDF/A Document")
c.setAuthor("John Doe")
c.setSubject("PDF/A Conversion")
c.setKeywords("pdf, pdf/a, conversion")

# Set the font and font size
c.setFont("fontname", 12)

# Draw the text on the canvas
c.drawString(100, 100, "Hello World!")

# Save the canvas
c.save()

# Close the canvas
c.showPage()
c.save()
