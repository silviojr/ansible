import requests
import json

# Base URL for the API (replace with your actual API endpoint)
base_url = "https://api.chromaticcultivation.com"

# Example `growthStage` data structure
growth_stage = {
    "stage": "flowering",
    "days_in_stage": 10,
    "color_development": "vibrant"
}

# Pod ID for the example
pod_id = "12345"

# Color intensity value for the example
color_intensity = 8

# 1. GET Request (hypothetically, to retrieve the current status before updating)
get_url = f"{base_url}/plants/{pod_id}/status"
response = requests.get(get_url)

if response.status_code == 200:
    print("Current plant status:", response.json())
else:
    print("Error fetching status:", response.status_code)

# 2. POST Request (if creating a new status record)
post_url = f"{base_url}/plants/{pod_id}/status"
data = {
    "growthStage": growth_stage,
    "colorIntensity": color_intensity
}
response = requests.post(post_url, json=data)

if response.status_code == 201:  # Assuming 201 Created for successful POST
    print("New status created successfully")
else:
    print("Error creating status:", response.status_code)

# 3. UPDATE Request (if modifying an existing status record)
update_url = f"{base_url}/plants/{pod_id}/status"
data = {
    "growthStage": growth_stage,
    "colorIntensity": color_intensity
}
response = requests.put(update_url, json=data) 

if response.status_code == 200:  # Assuming 200 OK for successful update
    print("Status updated successfully")
else:
    print("Error updating status:", response.status_code)