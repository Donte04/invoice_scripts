from pyxb import Unmarshaller

# Load the Factur-X invoice XML into a Python object
invoice_xml = open("invoice.xml", "r").read()
invoice = Unmarshaller.unmarshal(invoice_xml)

# Verify the signature of the invoice
if invoice.verify_signature():
    print("The signature of the invoice is valid.")
else:
    print("The signature of the invoice is not valid.")
