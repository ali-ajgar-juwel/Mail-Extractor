import requests, dns.resolver, re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from config import HEADERS, TIMEOUT, EMAIL_REGEX, CONTACT_KEYWORDS, EMAIL_PATTERNS

def get_domain(url):
    return urlparse(url if url.startswith("http") else "https://" + url).netloc.replace("www.", "")

def fetch_page(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        return BeautifulSoup(resp.text, "lxml") if resp.status_code == 200 else None
    except: return None

def extract_emails_from_soup(soup):
    text = soup.get_text(" ")
    html = str(soup)
    # সব ধরণের ইমেইল এক্সট্র্যাক্ট করবে
    found = set(EMAIL_REGEX.findall(text)) | set(EMAIL_REGEX.findall(html))
    return [e.lower().strip(".,;") for e in found if not any(x in e for x in [".png", ".jpg", ".svg", "example"])]

def extract_team_members(soup, domain):
    members = []
    containers = soup.find_all(['div', 'li', 'article', 'section'], class_=re.compile(r'team|member|profile|card|staff', re.I))
    for c in containers:
        name_tag = c.find(['h3', 'h4', 'h5', 'strong'], class_=re.compile(r'name|title', re.I))
        if name_tag:
            name = name_tag.get_text(strip=True)
            if 2 <= len(name.split()) <= 4:
                desc = name_tag.find_next_sibling()
                designation = desc.get_text(strip=True) if desc else "N/A"
                parts = name.lower().split()
                first, last = parts[0], parts[-1] if len(parts) > 1 else ""
                guessed = [p.format(first=first, last=last, domain=domain, f=first[0], l=last[0] if last else "") for p in EMAIL_PATTERNS]
                members.append({"name": name, "designation": designation, "guessed": guessed, "email": "Not Found", "status": "Unverified"})
    return members

def extract_leads(website_url):
    if not website_url.startswith("http"): website_url = "https://" + website_url
    domain = get_domain(website_url)
    
    result = {
        "company": domain.split(".")[0].upper(),
        "domain": domain,
        "website": website_url,
        "scraped_pages": [],
        "team_members": [],
        "direct_emails": []
    }
    
    home = fetch_page(website_url)
    if not home: return result
    
    pages = [website_url] + [urljoin(website_url, a['href']) for a in home.find_all('a', href=True) if any(kw in a['href'].lower() for kw in CONTACT_KEYWORDS)]
    
    # ডেটা সংগ্রহ
    for url in list(set(pages))[:5]:
        soup = fetch_page(url)
        if soup:
            result["scraped_pages"].append(url)
            # ১. সরাসরি ইমেইল সংগ্রহ
            result["direct_emails"].extend(extract_emails_from_soup(soup))
            # ২. টিম মেম্বার সংগ্রহ
            result["team_members"].extend(extract_team_members(soup, domain))
            
    result["direct_emails"] = list(set(result["direct_emails"]))
    
    # ৩. ম্যাচিং লজিক (নামের সাথে ইমেইল মেলানো)
    for m in result["team_members"]:
        for e in m["guessed"]:
            if e in result["direct_emails"]:
                m["email"], m["status"] = e, "Found on Site"
                break
    
    print(f"DEBUG: Found {len(result['direct_emails'])} direct emails and {len(result['team_members'])} members.")
    return result