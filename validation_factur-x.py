def verify_factur_X(factur_X_data):
    
    #check if all required fields are present in the factur-x data
    required_fields = ['invoice_number', 'invoice_date', 'total_amount', 'currency', 'seller_details', 'buyer_details']
    for field in required_fields:
        if field not in factur_X_data:
            return False

    #check if the invoice number is a valid format
    if not re.match(r'[A-Z]{2}[0-9]{9}', factur_X_data['invoice_number']):
        return False

    #check if the invoice date is a valid format
    try:
        datetime.datetime.strptime(factur_X_data['invoice_date'], '%Y-%m-%d')
    except ValueError:
        return False

    #check if the currency is a valid format
    if not re.match(r'[A-Z]{3}', factur_X_data['currency']):
        return False

    #check if the total amount is a valid format
    try:
        float(factur_X_data['total_amount'])
    except ValueError:
        return False

    #check if the seller and buyer details are in a valid format
    for party in ['seller_details', 'buyer_details']:
        if not isinstance(factur_X_data[party], dict):
            return False
    required_fields = ['name', 'street_address', 'postal_code', 'city', 'country']
    for field in required_fields:
        if field not in factur_X_data[party]:
            return False

    #if all checks pass, return True

    return True
