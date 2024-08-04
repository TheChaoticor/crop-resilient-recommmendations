import requests

# Your Flask API URL
api_url = "http://127.0.0.1:5000/add_crop"

# Initial crop data
initial_crops = [
    {"name": "Carrots", "soil_type": "Sandy"},
    {"name": "Radishes", "soil_type": "Sandy"},
    {"name": "Potatoes", "soil_type": "Sandy"},
    {"name": "Broccoli", "soil_type": "Clay"},
    {"name": "Cabbage", "soil_type": "Clay"},
    {"name": "Brussels Sprouts", "soil_type": "Clay"},
    {"name": "Lettuce", "soil_type": "Silty"},
    {"name": "Spinach", "soil_type": "Silty"},
    {"name": "Tomatoes", "soil_type": "Silty"},
    {"name": "Peas", "soil_type": "Peaty"},
    {"name": "Mint", "soil_type": "Peaty"},
    {"name": "Beans", "soil_type": "Peaty"},
    {"name": "Beetroot", "soil_type": "Chalky"},
    {"name": "Cabbage", "soil_type": "Chalky"},
    {"name": "Spinach", "soil_type": "Chalky"},
    {"name": "Corn", "soil_type": "Loamy"},
    {"name": "Soybeans", "soil_type": "Loamy"},
    {"name": "Wheat", "soil_type": "Loamy"}
]

# Function to add crops
def add_crops(crop_data):
    for crop in crop_data:
        response = requests.post(api_url, json=crop)
        if response.status_code == 201:
            print(f"Successfully added crop: {crop['name']}")
        else:
            print(f"Failed to add crop: {crop['name']} - {response.json()}")

# Add initial crops
add_crops(initial_crops)
