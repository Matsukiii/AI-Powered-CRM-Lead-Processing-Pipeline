🤖 AI-Powered CRM Lead Processing Pipeline

📌 Project Overview
An automated, end-to-end lead processing pipeline built with Make.com. This system catches raw lead data via webhooks, processes it through Google's Gemini AI to draft highly personalized sales copy, and automatically injects the enriched data into HubSpot CRM.

This eliminates manual data entry and provides sales teams with instant, context-aware email drafts the moment a new lead enters the system.

🏗️ Architecture & Tech Stack
Integration Engine: Make.com (formerly Integromat)

Trigger: Custom Webhook (REST API)

AI Processing: Google Gemini API (2.5 Flash)

Database/Destination: HubSpot CRM

Testing: Python (requests library)

⚙️ How It Works
Data Ingestion: A POST request containing the lead's Name, Business Type, and Current Challenge is fired to a Make.com webhook.

AI Orchestration: Make parses the JSON and maps the variables into a dynamic prompt sent to the Gemini 2.5 Flash endpoint.

Content Generation: Gemini writes a personalized, actionable cold email tailored to the lead's specific business challenge.

CRM Injection: The original lead data and the AI-generated email are mapped to HubSpot properties. A new Contact is created with a NEW Lead Status, ready for sales rep review.

💻 Testing the Webhook (Python Payload)
To simulate a form submission or incoming lead, this script fires the dummy data at the webhook:

import requests

# Make.com Webhook URL
webhook_url = "https://hook.make.com/YOUR_WEBHOOK_URL_HERE"

# Dummy lead data 
lead_data = {
    "name": "Jan Mar",
    "business_type": "Local Coffee Shop",
    "challenge": "We have great foot traffic in the morning, but it's completely dead after 2 PM."
}

# Fire the POST request
response = requests.post(webhook_url, json=lead_data)

if response.status_code == 200:
    print("Webhook successfully caught the data!")

📸 Proof of Concept

<img width="1178" height="421" alt="image" src="https://github.com/user-attachments/assets/f962830e-99b3-4bc9-ac01-9d28dc634930" />
<img width="1439" height="764" alt="image" src="https://github.com/user-attachments/assets/a18dbd61-1e5d-4db0-9f01-eac63334a72d" />
