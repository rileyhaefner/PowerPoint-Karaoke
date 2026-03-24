import requests
import io
import os
from PIL import Image
from dotenv import load_dotenv


#loads the virtual environment to get the API Key, this hides key like a password
load_dotenv()


#gets key from env then sets the value as a variable
HF_TOKEN = os.getenv("HF_TOKEN")


#the link to the API used on hugging face
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

#uses the api key on the website to generate
API_Key_check = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_AI_image(prompt):
    #gets input from below and pastes it into the api to create image
    prompt_name = {
        "inputs": prompt
    }
    #gets the image generated from the api
    create_in_web = requests.post(
        API_URL,
        headers=API_Key_check,    
        json=prompt_name
    )

    #saves and opens the image that the api created
    image = Image.open(io.BytesIO(create_in_web.content))
    image.save("test4.0.png")


#type text here to change the prompt
generate_AI_image("Rayyan in a house")
