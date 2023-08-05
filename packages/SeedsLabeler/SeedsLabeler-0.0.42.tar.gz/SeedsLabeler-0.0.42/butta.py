import requests
import json

image_path = "sample.jpg"
PROJECT_ID = "7"
# API_KEY = "0cda174e183667abd12e061e9ced3c0ecb008c52bd4830e7d293bd6847c211a4"
API_KEY = "d317c3f9bf95c0d68ace5db36a87be8eab9006ef1cc05908e27278c580728cde"
# url = "https://api-infer.thya-technology.com/api/v1/inference"
url = "https://prod-infer-train-backend.devcl.net/api/v1/inference"
headers = {
    # 'accept': '*/*',
    'x-api-key': API_KEY,
    # 'Content-Type': 'multipart/form-data'
}
files = {
    # 'projectId': PROJECT_ID,
    'projectId': (None, PROJECT_ID),
    'images': (image_path, open(image_path, 'rb'), 'image/jpeg') 
}

print(url)
print(headers)
print(files)

response = requests.request("POST", url, headers=headers, files=files)

print(response.status_code)
print(response.text)

# print(x)
# print(json.loads(x.text))