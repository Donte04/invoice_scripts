# Import the necessary libraries
from pyfacturx import FacturX

# Create a new Factur-X object
facturx = FacturX()

# Set the necessary metadata for the Factur-X
facturx.set_metadata(
    type="invoice", 
    version="1.0", 
    sender_name="Acme Corporation",
    sender_tax_id="123456789",
    sender_address="123 Main Street, Anytown, USA",
    receiver_name="John Doe",
    receiver_tax_id="987654321",
    receiver_address="456 Maple Street, Anytown, USA",
    invoice_number="INV-001",
    invoice_date="2022-01-01",
    payment_reference="PAY-001"
)

# Add items to the Factur-X
facturx.add_item("Product A", 1, 100)
facturx.add_item("Product B", 2, 50)

# Generate the Factur-X XML
facturx_xml = facturx.generate_xml()

# Save the Factur-X XML to a file
with open("facturx.xml", "w") as f:
    f.write(facturx_xml)
