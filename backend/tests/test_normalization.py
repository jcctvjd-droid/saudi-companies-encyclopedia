from __future__ import annotations

from app.services.normalization import normalize_arabic


def test_normalize_arabic_variants():
    assert normalize_arabic("شركة الإتصالات السعودية") == "شركة الاتصالات السعودية"
    assert normalize_arabic("أرامكو") == "ارامكو"
    assert normalize_arabic("مؤسسة") == "مؤسسة"
    assert normalize_arabic("  شركة   الاتصالات  ") == "شركة الاتصالات"


def test_normalize_empty_value():
    assert normalize_arabic("") == ""
