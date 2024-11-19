from openai import OpenAI
import json

openai_key = "YOUR_API_KEY"

# Function to query the AI with an image and get a detailed description
def get_image_description(image_url, image_type):
    client = OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"You are a real estate agent trying to describe the following feature of a property: {image_type}. Using the image provide a detail description of the feature."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    } 
                ]
            }            
        ],
        max_tokens=300,
    )
    return response

def collect_room_data():
    room_descriptions = {}
    while True:
        image_url = input("Enter the URL of the image:")
        image_type = input("Enter what the image is of (e.g. Exterior, Bathroom, Bedroom, etc.): ")
        description = get_image_description(image_url, image_type)
        room_descriptions[image_type] = description
        exit = input("Was that the final image? (y/n)")
        if exit == "y":
            break

    if room_descriptions:
        output_file = "room_data.txt"
        with open(output_file, "w") as f:
            f.write(json.dumps(room_descriptions))
        print(f"Data saved to {output_file}")
    else:
        print("No property data found.")
