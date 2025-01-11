import requests
import json

# Define the API key and URL for the property
geoapify_key = "YOUR_API_KEY"
url = f"https://api.geoapify.com/v2/places?categories=education.school,leisure.park,public_transport&filter=circle:151.086872,-33.891374,1000&bias=proximity:151.086872,-33.891374&limit=20&apiKey={geoapify_key}"

def collect_neighbourhood_data():
    response = requests.get(url)
    
    if response:
        output_file = "neighbourhood_data.txt"
        with open(output_file, "w") as f:
            f.write(json.dumps(response.json()))
        print(f"Data saved to {output_file}")
    else:
        print("No property data found.")