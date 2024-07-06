import google.generativeai as genai
import os

from DreamSearch import settings

genai.configure(api_key=os.environ['API_KEY'])

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("The opposite of hot is")
print(response.text)