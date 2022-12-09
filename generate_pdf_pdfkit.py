"""
1. Collect the necessary information for the invoice, such as the name and contact information of the client, the items or services being billed, the quantity of each item, the price of each item, and the total amount due.

2. Use a library like the pdfkit or reportlab library to generate the PDF invoice. These libraries allow you to create PDF documents using Python, and provide a variety of options for formatting and styling the invoice.

3. Use the collected information to populate the fields in the PDF invoice template. This can be done by using string formatting or template strings to insert the collected data into the appropriate places in the template.

4. Save the generated PDF invoice to a file or display it to the user.
"""
# Import the necessary libraries
import pdfkit

# Define the invoice template
template = """
<html>
<head>
<style>
...
</style>
</head>
<body>
<h1>Invoice</h1>
<p>Invoice Number: {invoice_number}</p>
<p>Invoice Date: {invoice_date}</p>
<p>Client Name: {client_name}</p>
<p>Client Address: {client_address}</p>
<h2>Items:</h2>
<table>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Price</th>
<th>Total</th>
</tr>
{items}
</table>
<p>Total Due: {total_due}</p>
</body>
</html>
"""

# Define the data for the invoice
invoice_number = 12345
invoice_date = "12/09/2022"
client_name = "John Doe"
client_address = "123 Main St, Anytown, USA"
items = [    ("Widget", 5, 10.00),    ("Gadget", 2, 5.00),]

# Calculate the total due
total_due = sum(qty * price for item, qty, price in items)

# Format the items as a table row
item_rows = "\n".join(
    f"<tr><td>{item}</td><td>{qty}</td><td>{price:.2f}</td><td>{qty * price:.2f}</td></tr>"
    for item, qty, price in items
)

# Populate the template with the data
html = template.format(
    invoice_number=invoice_number,
    invoice_date=invoice_date,
    client_name=client_name,
    client_address=client_address,
    items=item_rows,
    total_due=total_due,
)

# Generate the PDF invoice
pdf = pdfkit.from_string(html, False)

# Save the PDF invoice to a file
with open("invoice.pdf", "wb") as f:
    f.write(pdf)
