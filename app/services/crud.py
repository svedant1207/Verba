from sqlalchemy.orm import Session
from app.db import models

def create_document(db: Session, filename: str, content: str):
    db_document = models.Document(filename=filename, content=content)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def update_document_summary(db: Session, doc_id: int, summary: str):
    db_document = db.query(models.Document).filter(models.Document.id == doc_id).first()
    if db_document:
        db_document.summary = summary
        db.commit()
        db.refresh(db_document)
    return db_document

def get_document(db: Session, doc_id: int):
    return db.query(models.Document).filter(models.Document.id == doc_id).first()