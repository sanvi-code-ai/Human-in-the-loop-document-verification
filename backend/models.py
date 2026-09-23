from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean
from backend.database import Base

class RefernceInvoices(Base):
    __tablename__ = "reference_invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, nullable=False)
    vendor = Column(String, nullable=False)
    po_number = Column(String, nullable=False)
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    amount = Column(Numeric(12,2), nullable=False)
    currency = Column(String, nullable=False)

class UploadedInvoice(Base):
    __tablename__ = "uploaded_invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, nullable=False)
    vendor = Column(String, nullable=False)
    po_number = Column(String, nullable=False)
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String, nullable=False)

class VerificationResult(Base):
    __tablename__ = "verification_results"

    id = Column(Integer, primary_key=True, index=True)
    uploaded_invoice_id = Column(Integer, nullable=False)
    risk_score = Column(Integer, nullable=False)
    risk_level = Column(String, nullable=False)
    human_review_needed = Column(Boolean, nullable=False)
    status = Column(String, nullable=False)