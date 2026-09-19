from sqlalchemy import Column, Integer, String, Date, Numeric
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