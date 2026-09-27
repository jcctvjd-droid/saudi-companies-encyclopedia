from __future__ import annotations

from fastapi import APIRouter, Query

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/company")
def company_search(q: str = Query(...)):
    return {"q": q, "results": []}


@router.get("/suggestions")
def suggestions(q: str = Query(...)):
    return {"q": q, "suggestions": []}
