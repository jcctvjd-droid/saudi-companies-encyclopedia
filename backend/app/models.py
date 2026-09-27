from __future__ import annotations

from typing import List, Optional

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text, Date, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    arabic_name = Column(String(255), index=True)
    description = Column(Text, nullable=True)
    cities = relationship("City", back_populates="region")


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    arabic_name = Column(String(255), index=True)
    region_id = Column(Integer, ForeignKey("regions.id"), index=True)
    region = relationship("Region", back_populates="cities")
    companies = relationship("Company", back_populates="city")
    branches = relationship("Branch", back_populates="city")


class Sector(Base):
    __tablename__ = "sectors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    arabic_name = Column(String(255), index=True)
    description = Column(Text)
    companies = relationship("Company", back_populates="sector")


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    arabic_name = Column(String(255), index=True)
    description = Column(Text)
    companies = relationship("CompanyActivity", back_populates="activity")


class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    source_type = Column(String(50), nullable=False)
    url = Column(String(500), nullable=True)
    description = Column(Text)
    license = Column(String(255), nullable=True)
    last_checked_at = Column(DateTime, nullable=True)
    reliability_level = Column(String(50), default="medium")
    active = Column(Boolean, default=True)


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    arabic_name = Column(String(255), nullable=False, index=True)
    english_name = Column(String(255), nullable=True, index=True)
    normalized_arabic_name = Column(String(255), nullable=True, index=True)
    normalized_english_name = Column(String(255), nullable=True, index=True)
    legal_entity = Column(String(120), nullable=True)
    company_type = Column(String(100), nullable=True)
    status = Column(String(50), default="active")
    description = Column(Text)
    sector_id = Column(Integer, ForeignKey("sectors.id"), nullable=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=True, index=True)
    address = Column(Text, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    website = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    last_verified_at = Column(DateTime, nullable=True)
    data_quality_score = Column(Integer, default=0)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)

    sector = relationship("Sector", back_populates="companies")
    city = relationship("City", back_populates="companies")
    region = relationship("Region")
    activities = relationship("CompanyActivity", back_populates="company")
    branches = relationship("Branch", back_populates="company")
    commercial_registrations = relationship("CommercialRegistration", back_populates="company")
    company_sources = relationship("CompanySource", back_populates="company")


class CompanyActivity(Base):
    __tablename__ = "company_activities"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False, index=True)
    __table_args__ = (UniqueConstraint("company_id", "activity_id", name="uq_company_activity"),)
    company = relationship("Company", back_populates="activities")
    activity = relationship("Activity", back_populates="companies")


class Branch(Base):
    __tablename__ = "branches"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    branch_name = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=True, index=True)
    address = Column(Text, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    phone = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    status = Column(String(50), default="active")
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    company = relationship("Company", back_populates="branches")
    city = relationship("City", back_populates="branches")
    region = relationship("Region")


class CommercialRegistration(Base):
    __tablename__ = "commercial_registrations"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    registration_number = Column(String(100), index=True)
    registration_type = Column(String(100), nullable=True)
    issue_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)
    status = Column(String(50), default="active")
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    company = relationship("Company", back_populates="commercial_registrations")


class CompanySource(Base):
    __tablename__ = "company_sources"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False, index=True)
    source_type = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=True)
    company = relationship("Company", back_populates="company_sources")
    source = relationship("Source")


class CompanyHistory(Base):
    __tablename__ = "company_history"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    field_name = Column(String(120), nullable=False, index=True)
    old_value = Column(Text, nullable=True)
    new_value = Column(Text, nullable=True)
    changed_at = Column(DateTime, nullable=True)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)
    reason = Column(Text, nullable=True)


class CompanyContact(Base):
    __tablename__ = "company_contacts"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    contact_type = Column(String(80), nullable=True)
    value = Column(String(255), nullable=True)
    is_public = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)


class CompanyWebsite(Base):
    __tablename__ = "company_websites"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    url = Column(String(500), nullable=False)
    site_type = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)


class CompanyIdentifier(Base):
    __tablename__ = "company_identifiers"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    identifier_type = Column(String(80), nullable=False)
    identifier_value = Column(String(255), nullable=False)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)


class DataImport(Base):
    __tablename__ = "data_imports"
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=True)
    import_name = Column(String(255), nullable=False)
    source_format = Column(String(50), nullable=False)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)


class DataImportRecord(Base):
    __tablename__ = "data_import_records"
    id = Column(Integer, primary_key=True, index=True)
    import_id = Column(Integer, ForeignKey("data_imports.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)
    record_status = Column(String(50), default="pending")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=True)


class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String(120), nullable=False)
    entity_type = Column(String(80), nullable=False)
    entity_id = Column(Integer, nullable=True)
    actor = Column(String(200), nullable=True)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=True)
