import requests

# Assuming the API endpoint is at 'https://api.chromaticcultivation.com'
base_url = 'https://api.chromaticcultivation.com'

# Replace with actual values
pod_id = '12345'
harvest_date = '2024-08-25'

# Construct the URL for the API call
url = f'{base_url}/harvest-extraction/generatePigmentProfile?podID={pod_id}&harvestDate={harvest_date}'

# Make the GET request
response = requests.get(url)

def hex_to_rgb(hex_color):
    """Converts a hex color code to RGB values."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response    1.  github.com github.com
    pigment_profile = response.json()

    # Print all the fields in the pigment profile
    print("Pod ID:", pigment_profile['podID'])
    print("Harvest Date:", pigment_profile['harvestDate'])
    print("Color Name:", pigment_profile['colorName'])
    print("Color Hex Code:", pigment_profile['colorHex'])
    print("Lightfastness Rating:", pigment_profile['lightfastness'])
    print("Transparency:", pigment_profile['otherProperties']['transparency'])
    print("Granulation:", pigment_profile['otherProperties']['granulation'])
else:
    print(f"Error: {response.status_code} - {response.text}")



base_url = 'https://api.chromaticcultivation.com'


url = f'{base_url}/harvest-extraction/generatePigmentProfile?podID=3492&harvestDate="2024-08-25"'

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response    1.  github.com github.com
    pigment_profile = response.json()
    print("Color Hex Code:", pigment_profile['colorHex'])
    # convert hex to RGB
    print("RGB:", hex_to_rgb(pigment_profile['colorHex']))
else:
    print(f"Error: {response.status_code} - {response.text}")

