import requests

color_range = {
    "colorRange": ["warm", "earth tones"]  # Include multiple color ranges
}

response = requests.get(
    "https://chromaticcultivation.com/api/podCatalog/getPodVarieties",
    params={"season": "summer"},
    json=color_range
)

if response.status_code == 200:
    pod_varieties = response.json()["availableVarieties"]
    for variety in pod_varieties:
        print(f"Name: {variety['name']}, Color Range: {variety['colorRange']}")
else:
    print(f"Error: {response.status_code}")