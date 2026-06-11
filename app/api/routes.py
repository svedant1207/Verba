from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.document import DocumentResponse
from app.services import crud, summarizer

router = APIRouter()


@router.post("/upload/", response_model=DocumentResponse)
async def upload_and_summarize(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Read file content
    content = await file.read()
    text_content = content.decode("utf-8")

    # Save document to DB
    document = crud.create_document(db=db, filename=file.filename, content=text_content)

    # Generate summary
    try:
        summary_text = summarizer.summarize_text(text_content)
        # Update DB with summary
        updated_document = crud.update_document_summary(db=db, doc_id=document.id, summary=summary_text)
        return updated_document
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/documents/{doc_id}", response_model=DocumentResponse)
def read_document(doc_id: int, db: Session = Depends(get_db)):
    document = crud.get_document(db, doc_id=doc_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document