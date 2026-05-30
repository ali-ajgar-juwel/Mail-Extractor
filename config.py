import re

# ─── CONFIGURATION ───────────────────────────────────────────────

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

TIMEOUT = 10

# ইমেইল খোঁজার রেগুলার এক্সপ্রেশন
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

# টিম পেজ খোঁজার জন্য কিওয়ার্ড
CONTACT_KEYWORDS = ["contact", "about", "team", "staff", "people", "who-we-are", "our-team"]

# ডেজিগনেশন ফিল্টারিং কিওয়ার্ড
DESIGNATION_KEYWORDS = [
    "ceo", "chief executive", "founder", "co-founder",
    "cto", "chief technology", "coo", "chief operating",
    "cfo", "chief financial",
    "vp", "vice president",
    "director",
    "manager",
    "hr", "human resources", "recruitment", "talent",
    "sales", "business development", "bd",
    "marketing",
    "president",
    "head of",
    "lead",
    "partner",
]

# ইমেইল ফরম্যাট জেনারেশন প্যাটার্ন
EMAIL_PATTERNS = [
    "{first}@{domain}",
    "{first}.{last}@{domain}",
    "{f}{last}@{domain}",
    "{first}{last}@{domain}",
    "{first}_{last}@{domain}",
    "{first}-{last}@{domain}",
    "{f}.{last}@{domain}",
    "{first}{l}@{domain}",
]

# হেডিং বা লাইন ফিল্টার করার জন্য এক্সক্লুশন লিস্ট
SKIP_WORDS = [
    'information', 'experience', 'solutions', 'services', 
    'optimization', 'expertise', 'america', 'contact', 
    'support', 'overview', 'management'
]