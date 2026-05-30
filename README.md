Mail Scraper & Exporter System 

This project is an automated Python-based tool designed to perform web scraping on company websites to collect team member names, designations, and verified email addresses. The collected data is automatically processed and exported into a structured .xlsx (Excel) file.

Key Features

Web Scraping: Automatically targets and extracts team member profiles (names and titles) from company websites.

Smart Mapping: Intelligently maps guessed email patterns to the specific team members found on the page.

Data Export: Neatly organizes and saves the data into Summary and Leads sheets in an Excel file.

Email Verification: Validates the collected emails by checking domain MX records to ensure deliverability.



Tech Stack
Python: Core logic and automation.

BeautifulSoup4: For parsing HTML and extracting information.

Openpyxl: For generating and formatting Excel files.

Requests & DNS: For web page fetching and email server validation.

Project Structure
main.py: The entry point to execute the scraping system.

scraper.py: Core logic for web scraping, data extraction, and email mapping.

exporter.py: Handles the generation and saving of the Excel reports.

config.py: Configuration file for headers, email patterns, and keywords.



How to Use
Clone the repository:

Bash
git clone https://ali-ajgar-juwel.github.io/Mail-Extractor/
Install the required dependencies:

Bash
pip install -r requirements.txt
Run the system:

Bash
python main.py
Enter the URL: Provide the website address when prompted by the terminal to start the extraction process.

Important Note
This tool is intended for educational purposes and legitimate professional lead generation.

Please ensure compliance with the target website's robots.txt and terms of service before scraping.

License
This project is open-source. Feel free to use it or contribute to its development.
