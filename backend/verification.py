def compare_invoices(reference_invoice, uploaded_invoice):
    mismatches = {}

    if reference_invoice.invoice_number != uploaded_invoice.invoice_number:
        mismatches["invoice_number"] = True

    if reference_invoice.vendor != uploaded_invoice.vendor:
        mismatches["vendor"] = True

    if reference_invoice.po_number != uploaded_invoice.po_number:
        mismatches["po_number"] = True

    if reference_invoice.invoice_date != uploaded_invoice.invoice_date:
        mismatches["invoice_date"] = True

    if reference_invoice.due_date != uploaded_invoice.due_date:
        mismatches["due_date"] = True

    if reference_invoice.amount != uploaded_invoice.amount:
        mismatches["amount"] = True

    if reference_invoice.currency != uploaded_invoice.currency:
        mismatches["currency"] = True

    return mismatches


from backend.models import RefernceInvoices, UploadedInvoice


def verify_invoice(db, uploaded_invoice_id):
    uploaded_invoice = db.query(UploadedInvoice).filter(
        UploadedInvoice.id == uploaded_invoice_id
    ).first()

    if not uploaded_invoice:
        return {"error": "Uploaded invoice not found"}

    reference_invoice = db.query(RefernceInvoices).filter(
        RefernceInvoices.invoice_number == uploaded_invoice.invoice_number
    ).first()

    if not reference_invoice:
        return {"error": "Reference invoice not found"}

    mismatches = compare_invoices(reference_invoice, uploaded_invoice)

    return mismatches
