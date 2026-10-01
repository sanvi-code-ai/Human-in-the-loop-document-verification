from backend.database import SessionLocal
from backend.verification import verify_invoice

db = SessionLocal()

result = verify_invoice(db, 1)

print(result)

db.close()