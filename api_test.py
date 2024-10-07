import os
from groq import Groq
from deepgram import Deepgram

# Load environment variables
from dotenv import load_dotenv
load_dotenv('.env.local')

def test_groq_api():
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say hello!",
            }
        ],
        model="mixtral-8x7b-32768",
    )
    print("GROQ API Response:", chat_completion.choices[0].message.content)

def test_deepgram_api():
    deepgram = Deepgram(os.environ["DEEPGRAM_API_KEY"])
    
    # URL of a sample audio file
    url = "https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav"

    response = deepgram.transcription.sync_prerecorded(
        {"url": url},
        {
            "smart_format": True,
            "model": "general",
        },
    )
    print("Deepgram API Response:", response["results"]["channels"][0]["alternatives"][0]["transcript"])

if __name__ == "__main__":
    print("Testing GROQ API...")
    test_groq_api()
    print("\nTesting Deepgram API...")
    test_deepgram_api()