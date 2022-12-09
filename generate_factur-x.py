# Import the necessary libraries
import facturx

# Create a new Factur-X invoice object
invoice = facturx.Invoice()

# Set the invoice number
invoice.invoice_number = "123456"

# Set the customer information
invoice.customer_name = "John Doe"
invoice.customer_street = "123 Main Street"
invoice.customer_postal_code = "12345"
invoice.customer_city = "Anytown"
invoice.customer_country = "US"

# Add an item to the invoice
item = facturx.Item()
item.name = "Widget"
item.quantity = 10
item.unit_price = 9.99
invoice.items.append(item)

# Generate the Factur-X XML
facturx_xml = invoice.to_facturx()

# Save the XML to a file
with open("facturx.xml", "w") as f:
  f.write(facturx_xml)
