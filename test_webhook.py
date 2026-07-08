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
