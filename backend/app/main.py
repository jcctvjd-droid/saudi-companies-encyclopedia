from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.database import Base, engine, get_db
from app.models import Activity, Branch, City, Company, CompanyActivity, CompanySource, Region, Sector, Source
from app.services.normalization import normalize_arabic, normalize_query
from app.data.demo import DEMO_COMPANIES

app = FastAPI(title="Saudi Companies Encyclopedia API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/api/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/companies")
def companies(q: str | None = None, sector: str | None = None, city: str | None = None, page: int = 1, page_size: int = 20):
    items = []
    for company in DEMO_COMPANIES:
        if q and normalize_query(q) not in normalize_query(company["arabic_name"] + " " + (company["english_name"] or "")):
            continue
        if sector and normalize_query(sector) not in normalize_query(company["sector"]):
            continue
        if city and normalize_query(city) not in normalize_query(company["city"]):
            continue
        items.append({
            "id": company["id"],
            "arabic_name": company["arabic_name"],
            "english_name": company["english_name"],
            "sector": company["sector"],
            "city": company["city"],
            "company_type": company["company_type"],
            "status": company["status"],
            "website": company["website"],
            "branch_count": 1,
            "updated_at": company["updated_at"],
        })
    start = (page - 1) * page_size
    end = start + page_size
    return {"items": items[start:end], "page": page, "page_size": page_size, "total": len(items), "total_pages": max(1, (len(items) + page_size - 1) // page_size) if items else 0}


@app.get("/api/v1/companies/{company_id}")
def company_detail(company_id: int):
    for company in DEMO_COMPANIES:
        if company["id"] == company_id:
            return company
    return JSONResponse(status_code=404, content={"detail": "Company not found"})


@app.get("/api/v1/companies/{company_id}/branches")
def company_branches(company_id: int):
    return [{"id": 1, "branch_name": "الفرع الرئيسي", "city": "الرياض", "status": "active"}]


@app.get("/api/v1/companies/{company_id}/activities")
def company_activities(company_id: int):
    return [{"id": 1, "name": "الاتصالات"}]


@app.get("/api/v1/companies/{company_id}/sources")
def company_sources(company_id: int):
    return [{"id": 1, "source_name": "DEMO SOURCE", "source_type": "demo"}]


@app.get("/api/v1/sectors")
def sectors():
    return [{"id": 1, "name": "الاتصالات"}, {"id": 2, "name": "النفط والغاز"}, {"id": 3, "name": "البنوك"}]


@app.get("/api/v1/cities")
def cities():
    return [{"id": 1, "name": "الرياض"}, {"id": 2, "name": "الظهران"}]


@app.get("/api/v1/regions")
def regions():
    return [{"id": 1, "name": "الرياض"}, {"id": 2, "name": "الشرق"}]


@app.get("/api/v1/activities")
def activities():
    return [{"id": 1, "name": "الاتصالات"}, {"id": 2, "name": "التعبئة"}]


@app.get("/api/v1/search/suggestions")
def suggestions(q: str):
    matches = [company for company in DEMO_COMPANIES if q.lower() in (company["arabic_name"] + " " + (company["english_name"] or "")).lower()]
    return {"items": [{"id": c["id"], "label": c["arabic_name"], "english_name": c["english_name"]} for c in matches[:10]]}


@app.get("/api/v1/companies/nearby")
def nearby_companies(latitude: float, longitude: float, radius: float = 5000, page: int = 1, page_size: int = 20):
    items = []
    for company in DEMO_COMPANIES:
        if company.get("latitude") is None or company.get("longitude") is None:
            continue
        distance = ((company["latitude"] - latitude) ** 2 + (company["longitude"] - longitude) ** 2) ** 0.5 * 111000
        if distance <= radius:
            items.append({"id": company["id"], "arabic_name": company["arabic_name"], "distance_meters": round(distance, 2)})
    start = (page - 1) * page_size
    end = start + page_size
    return {"items": items[start:end], "page": page, "page_size": page_size, "total": len(items), "total_pages": max(1, (len(items) + page_size - 1) // page_size) if items else 0}
