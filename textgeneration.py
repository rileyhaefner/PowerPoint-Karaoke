import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
print(os.environ['HF_TOKEN'])
headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

prompt = str(input("Enter a presentation topic: "))
response = query({
    "messages": [
        {
            "role": "user",
            "content": "Make a short horribly-written presentation-style paragraph on " + prompt + ". Make only one draft"
        }
    ],
    "model": "zai-org/GLM-5:novita"
})
print(response)

print(response["choices"][0]["message"])
