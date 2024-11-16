import os
import requests
from PIL import Image
from io import BytesIO

def generate_image():
    try:
        # Define the path to save the image
        file_path = os.path.join("assets", "a.png")

        # Ensure the directory exists
        if not os.path.exists("assets"):
            os.makedirs("assets")
            print(f"Created 'assets' directory.")

        # Unsplash API key (sign up for free at https://unsplash.com/developers)
        api_key = 'sUj4fzEgULgiZOWa3uL_1I-_Lzvolx6YCadhutc09f8'  # Replace with your Unsplash API key
        url = "https://api.unsplash.com/photos/random"

        # Define the search query or keyword (you can change the prompt to whatever you want)
        query = "nature landscape"  # You can change this to any keyword like "mountains", "beach", etc.

        # Send a request to the Unsplash API to get a random photo based on the query
        response = requests.get(
            url,
            params={
                'query': query,
                'client_id': api_key,  # Unsplash API requires 'client_id' for authentication
                'orientation': 'landscape'  # Optional: to get landscape-oriented images
            }
        )

        # Check if the response is successful
        if response.status_code == 200:
            # Get the image URL from the response
            image_url = response.json()[0]['urls']['regular']

            # Download the image
            img_data = requests.get(image_url).content
            img = Image.open(BytesIO(img_data))

            # Save the image locally
            img.save(file_path)
            print(f"Image generated and saved at {file_path}")
        else:
            print(f"Error fetching image: {response.status_code}")
            print(f"Response text: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
