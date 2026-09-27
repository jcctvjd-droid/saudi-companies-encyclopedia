from __future__ import annotations

import re

ARABIC_MAP = {
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ة": "ة",
    "ى": "ي",
    "ي": "ي",
    "ئ": "ي",
    "ؤ": "و",
    "أ": "ا",
    "إ": "ا",
    "ْ": "",
    "ٌ": "",
    "ً": "",
    "ٍ": "",
    "ـ": "",
    "\u200c": "",
    "\u200d": "",
}


def normalize_arabic(value: str) -> str:
    if not value:
        return ""
    text = value.strip().lower()
    for source, target in ARABIC_MAP.items():
        text = text.replace(source, target)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[\t\n\r]+", " ", text)
    text = text.strip()
    return text


def normalize_query(value: str) -> str:
    if not value:
        return ""
    text = normalize_arabic(value)
    return text.replace(" ", " ").strip()
