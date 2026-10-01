from backend.models import RefernceInvoices, UploadedInvoice
from backend.verification import compare_invoices
from datetime import date
from decimal import Decimal

reference = RefernceInvoices(
    invoice_number="INV001",
    vendor="ABC Ltd",
    po_number="PO1001",
    invoice_date=date(2026, 9, 10),
    due_date=date(2026, 10, 10),
    amount=Decimal("50000.00"),
    currency="INR"
)

uploaded = UploadedInvoice(
    invoice_number="INV001",
    vendor="ABC Ltd",
    po_number="PO1001",
    invoice_date=date(2026, 9, 10),
    due_date=date(2026, 10, 10),
    amount=Decimal("55000.00"),
    currency="INR"
)

result = compare_invoices(reference, uploaded)

print(result)