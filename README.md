# LinkedIn Job Details Scraper using Selenium and Python

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Selenium Version](https://img.shields.io/badge/selenium-3.x-green.svg)

This is a Python project that utilizes the Selenium framework to scrape job details from LinkedIn job listings. The script automates the process of navigating through job listings, extracting relevant information, and saving it to a CSV file for further analysis.

Please note that web scraping might be against the terms of service of some websites, including LinkedIn. Make sure to review LinkedIn's terms of use before using this script extensively. This project is intended for educational and personal use only.

## Features

- Automated login to LinkedIn using environment variables for credentials.
- Search for specific job titles and locations.
- Extract job details including job title, company name, location, and job description.
- Save the extracted data to a CSV file for easy analysis.

## Prerequisites

- Python 3.x: Make sure you have Python 3.x installed on your system.
- Selenium: Install Selenium using `pip install selenium`.
- Chrome WebDriver: Download the Chrome WebDriver compatible with your Chrome browser version and place it in the project directory.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/linkedin-job-scraper.git
cd linkedin-job-scraper
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Place the downloaded Chrome WebDriver executable (chromedriver.exe) in the project directory.

4. Set up environment variables for your LinkedIn credentials:

```bash
export LINKEDIN_EMAIL="your_email@example.com"
export LINKEDIN_PASSWORD="your_password"
```

5. Modify the search parameters in the `main.py` file:

```python
# Modify the search parameters
job_title = "Software Engineer"
```

6. Run the script:

```bash
python main.py
```

7. The script will automatically use the environment variables for LinkedIn credentials, perform the job search, scrape job details, and save them to a CSV file named `job_details.csv`.


## Disclaimer

This project is for educational and personal use only. Use it responsibly and make sure to review LinkedIn's terms of use before using this script extensively.

---

Feel free to ask if you have any questions or need further assistance!
