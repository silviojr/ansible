import requests
import json


# sample of calling the pod status API
def sample_get_pod_status_API():
    # Base URL for the API (replace with your actual API endpoint)
    base_url = "https://api.chromaticcultivation.com"

    # Pod ID for the example
    pod_id = "12345"

    get_url = f"{base_url}/plants/{pod_id}/status"



    # 1. GET Request (hypothetically, to retrieve the current status before updating)
    response = requests.get(get_url)

    if response.status_code == 200:
        print("Current plant status:", response.json())
    else:
        print("Error fetching status:", response.status_code)

def sample_post_pod_status_API():
    base_url = "https://api.chromaticcultivation.com"
    pod_id = "12345"
    
    # POST Request (if creating a new status record)
    post_url = f"{base_url}/plants/{pod_id}/status"
    
    # Example `growthStage` data structure
    growth_stage = {
        "stage": "flowering",
        "days_in_stage": 10,
        "color_development": "vibrant"
    }
    
    # Color intensity value for the example
    color_intensity = 8

    data = {
        "growthStage": growth_stage,
        "colorIntensity": color_intensity
    }
    response = requests.post(post_url, json=data)

    if response.status_code == 201:  # Assuming 201 Created for successful POST
        print("New status created successfully")
    else:
        print("Error creating status:", response.status_code)