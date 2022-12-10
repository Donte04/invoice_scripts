import xml.etree.ElementTree as ET
import base64
import hashlib

def verify_factur_x(invoice_xml):
  # parse the XML invoice
  invoice = ET.fromstring(invoice_xml)
  
  # find the SignedSignature element
  signed_signature_element = invoice.find(".//*[@Id='SignedSignature']")
  
  # get the signature value and signed properties
  signature_value = base64.b64decode(signed_signature_element.find(".//*[@Id='SignatureValue']").text)
  signed_properties = base64.b64decode(signed_signature_element.find(".//*[@Id='SignedProperties']").text)
  
  # get the references
  references = signed_signature_element.findall(".//*[@URI]")
  
  # create a dictionary mapping reference URIs to their base64-encoded hashes
  reference_dict = {}
  for ref in references:
    uri = ref.get('URI')
    if uri.startswith('#'):
      uri = uri[1:]
    digest_method = ref.find(".//*[@Algorithm]").get('Algorithm')
    digest_value = base64.b64decode(ref.find(".//*[@DigestValue]").text)
    if digest_method == 'http://www.w3.org/2001/04/xmlenc#sha256':
      # compute the SHA-256 hash of the element with the specified ID
      element = invoice.find(f".//*[@Id='{uri}']")
      if element is not None:
        sha256 = hashlib.sha256()
        sha256.update(ET.tostring(element))
        digest = sha256.digest()
        reference_dict[uri] = base64.b64encode(digest)
  
  # create a list of references to verify
  to_verify = [signed_properties] + list(reference_dict.values())
  
  # verify the signature
  from OpenSSL import crypto
  x509 = crypto.load_pkcs7_data(crypto.FILETYPE_ASN1, signature_value)
  store = crypto.X509Store()
  for cert in x509.get0_certificates():
      store.add_cert(cert)
  ctx = crypto.X509StoreContext(store, x509)
  try:
      ctx.verify_certificate()
  except Exception as e:
      print(f"Error verifying certificate: {e}")
      return False

  # return whether the signature is valid
  return True
