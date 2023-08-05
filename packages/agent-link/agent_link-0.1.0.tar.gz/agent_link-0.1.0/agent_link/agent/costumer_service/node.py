import os
import json
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, send_from_directory
from gtts import gTTS
import io
from google.cloud import speech_v1 as speech
from google.cloud.speech_v1 import RecognitionConfig, RecognitionAudio
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../key/firebase.json"

# Load company details from JSON file
with open("./data/company_details.json") as f:
    company_data = json.load(f)

@app.route("/api/v1/chat", methods=["POST"])
def chat():
    user_input = request.json["content"]

    # Get response from the chatbot
    response_text = generate_response(user_input)

    # Convert the chatbot's response to speech
    tts = gTTS(response_text, lang="en")
    tts.save("response.mp3")

    return jsonify({"response_text": response_text})

@app.route("/api/v1/voice_chat", methods=["POST"])
def voice_chat():
    # Get audio from the request
    audio_file = request.files["audio"]

    # Convert the audio to text using Google Cloud Speech-to-Text
    client = speech.SpeechClient()
    file_content = audio_file.read()
    audio = types.RecognitionAudio(content=file_content)

    config = RecognitionConfig(
        encoding=RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )


    response = client.recognize(config, audio)
    transcript = response.results[0].alternatives[0].transcript

    # Get response from the chatbot
    response_text = generate_response(transcript)

    # Convert the chatbot's response to speech
    tts = gTTS(response_text, lang="en")
    tts.save("response.mp3")

    with open("response.mp3", "rb") as f:
        mp3_data = f.read()

    return mp3_data, 200, {"Content-Type": "audio/mpeg"}

def generate_response(user_input):
    # Check if the user is asking about a product
    for product in company_data["products"]:
        if product.lower() in user_input.lower():
            return f"We have the {product} on our menu. Do you want to know more about it or order it?"

    # Check if the user is asking about a service
    for service in company_data["services"]:
        if service.lower() in user_input.lower():
            return f"We offer {service} service. Do you want to know more about it?"

    # Check if the user is asking an FAQ
    for faq in company_data["faqs"]:
        if faq["question"].lower() in user_input.lower():
            return faq["answer"]
        
    # Generate a response using the GPT-4 model
    messages = [
        {"role": "system", "content": f"Welcome to {company_data['name']} Customer Support! My name is McBot. How can I help you today?"},
        {"role": "user", "content": user_input}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message["content"]

if __name__ == "__main__":
    app.run(debug=True)
