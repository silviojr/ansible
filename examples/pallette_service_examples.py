import requests

pigmentProfile = {
    "podID": "PP-12345",
    "harvestDate": "2024-08-25",
    "colorName": "Sunset Gold",
    "colorHex": "#F2C94C",
    "lightfastness": 8,
    "otherProperties": {
        "transparency": "semi-transparent",
        "granulation": "medium"
    }
}

artworkImage = open("my_artwork.jpg", "rb")  # Assuming you have an artwork image ready

response = requests.post(
    "https://api.chromaticcultivation.com/communityPalette/sharePigmentProfile",
    json=pigmentProfile,
    files={"artworkImage": artworkImage}
)

if response.status_code == 200:
    print("Pigment profile and artwork shared successfully!")
else:
    print(f"Error sharing: {response.status_code} - {response.text}")




response = requests.post(
    "https://api.chromaticcultivation.com/communityPalette/sharePigmentProfile",
    json={
        "podID": "PP-54321",
        "harvestDate": "2024-07-15",
        "colorName": "Crimson Clarity",
        "colorHex": "#DC143C",
        "lightfastness": 9,
        "otherProperties": {
            "transparency": "high",
            "granulation": "none"
        }
    },
    files={"artworkImage": open("watercolor_sunset.jpg", "rb")}
)




