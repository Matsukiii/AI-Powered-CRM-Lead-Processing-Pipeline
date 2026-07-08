import requests

# Replace with your actual Make.com Webhook URL
webhook_url = "https://hook.eu1.make.com/csmk1nu8kixsff7is8q28infnbj9k864"

# Our dummy lead data from a hypothetical San Jose business
lead_data = {
    "name": "Jan Mar",
    "business_type": "Local Coffee Shop",
    "challenge": "We have great foot traffic in the morning, but it's completely dead after 2 PM."
}

response = requests.post(webhook_url, json=lead_data)

print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print("Webhook successfully caught the data!")