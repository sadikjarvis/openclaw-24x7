import requests
import sys
import json

# Take prompt from command line
prompt = " ".join(sys.argv[1:])

API_KEY = "AIzaSyDfheMbps8muuk-GTSjyv4WmdqqssqO-Ig"
API_URL = "https://api.nanobanana.com/v1/generate"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "prompt": prompt,
    "options": {"max_tokens": 500}  # adjust for images if needed
}

response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
data = response.json()

# Print URL or base64 returned by Nano Banana
print(data.get("image_url") or data.get("image_base64") or "No output returned")
