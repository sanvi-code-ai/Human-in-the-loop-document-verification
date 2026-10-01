from backend.database import SessionLocal
from backend.models import UploadedInvoice

db = SessionLocal()

invoice = db.query(UploadedInvoice).first()

print(invoice.id)
print(invoice.invoice_number)
print(invoice.amount)

db.close()