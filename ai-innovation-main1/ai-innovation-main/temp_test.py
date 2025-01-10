import requests
import json


BASE_URL = "http://100.103.35.20:1337/v1"
CHAT_ENDPOINT = "/chat/completions"
MODEL = "Replete-LLM-V2.5-Qwen-32b-IQ4_XS.gguf"

with open("data/students/sample_student.json", encoding="utf-8") as f:
    student_data = json.load(f)

with open("data/cs_roadmap/roadmap.json", encoding="utf-8") as f:
    roadmap = json.load(f)


data = {
    "messages": [
        {
            "content": "You are an college advisor.",
            "role": "system"
        },
        {
            "content": "Here is the student's degreeworks: " + str(student_data),
            "role": "system"
        },
        {
        
            "content": "Here is their roadmap to graduate: " + str(roadmap),
            "role": "system"
        },
        {
            "content": input("Enter your user prompt: "),
            "role": "user"
        }
    ],
    "model": MODEL,
    "max_tokens": 2048,
}

response = requests.post(BASE_URL + CHAT_ENDPOINT, json=data, stream=True)
print(response.json())
# print(roadmap)