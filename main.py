import sys
import os
from datetime import datetime
from scraper import extract_leads, get_domain  # scraper.py থেকে ইমপোর্ট
from exporter import save_to_excel            # exporter.py থেকে ইমপোর্ট

def run_scraper():
    # ইউজার ইনপুট বা আর্গুমেন্ট হ্যান্ডলিং
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter website URL: ").strip()

    if not url:
        print("❌ Error: Website URL is required.")
        return

    # ডেটা এক্সট্রাকশন (সব লজিক scraper.py তে)
    print(f"\n🚀 Starting lead extraction for: {url}")
    data = extract_leads(url)

    # এক্সেল ফাইল সেভ করার প্রস্তুতি
    domain = get_domain(url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_domain = domain.replace(':', '_').replace('/', '_')
    out_file = os.path.join(os.getcwd(), f"{safe_domain}_{timestamp}.xlsx")

    # এক্সেল এক্সপোর্ট (exporter.py ব্যবহার করে)
    save_to_excel(data, out_file)

    # Final console output
    print("\n" + "="*50)
    print(f"  COMPANY    : {data['company']}")
    print(f"  DOMAIN     : {data['domain']}")
    
    # Direct Emails list show korar jonno
    print(f"  DIRECT EMAILS FOUND ({len(data['direct_emails'])}):")
    if data['direct_emails']:
        for e in data['direct_emails']:
            print(f"    • {e}")
    else:
        print("    (No direct emails found)")

    # Team Members & Verified Emails list show korar jonno
    print(f"\n  TEAM MEMBERS ({len(data['team_members'])}):")
    for m in data['team_members']:
        email_status = m['verified_email'] if m['verified_email'] else "Unverified"
        print(f"    • {m['name']} | {m['designation']} | {email_status}")
    
    print("="*50)

if __name__ == "__main__":
    run_scraper()