import os
import requests
from dotenv import load_dotenv

load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_TOKEN")

if not APIFY_TOKEN:
    print("ERROR: APIFY_TOKEN .env file me nahi mila")
    raise SystemExit

actor_id = "apify~web-scraper"

url = (
    f"https://api.apify.com/v2/acts/{actor_id}"
    f"/run-sync-get-dataset-items?token={APIFY_TOKEN}"
)

payload = {
    "startUrls": [
        {
            "url": "https://wttr.in/Dehradun?format=3"
        }
    ],
    "pageFunction": """
    async function pageFunction(context) {
        const { request, log } = context;

        log.info(`Scraping ${request.url}`);

        return {
            city: "Dehradun",
            weather_text: document.body.innerText.trim(),
            source_url: request.url,
            scraped_at: new Date().toISOString()
        };
    }
    """,
    "maxRequestsPerCrawl": 1
}

response = requests.post(
    url,
    json=payload,
    timeout=120
)

print("STATUS:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("\nWEATHER DATA:")
    print(data)
else:
    print("\nERROR:")
    print(response.text)