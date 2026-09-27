from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import Company
from app.services.normalization import normalize_query

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/suggestions")
def search_suggestions(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    normalized = normalize_query(q)
    companies = db.query(Company).filter(
        Company.normalized_arabic_name.ilike(f"%{normalized}%")
        | Company.normalized_english_name.ilike(f"%{normalized}%")
        | Company.arabic_name.ilike(f"%{q}%")
    ).limit(10).all()
    return {"items": [{"id": c.id, "label": c.arabic_name, "english_name": c.english_name} for c in companies]}
