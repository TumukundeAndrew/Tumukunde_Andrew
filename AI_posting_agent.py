import os
import time
import requests
from dotenv import load_dotenv
import tweepy

load_dotenv()

# Load credentials from environment
API_KEY = os.getenv('X_API_KEY')
API_SECRET = os.getenv('X_API_SECRET')
ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('X_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('X_BEARER_TOKEN')

# AI model API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions'

# Initialize Tweepy v2 client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def generate_ai_content(prompt, retries=3, backoff=5):
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
    "model": "gpt-3.5-turbo",  
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 100,
    "temperature": 0.7
}


    def call_openai_api(data, retries=5, initial_backoff=5):
     backoff = initial_backoff
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(OPENAI_API_URL, json=data, headers=headers)
            response.raise_for_status()
            content = response.json()['choices'][0]['message']['content'].strip()
            return content
        except requests.exceptions.HTTPError as e:
            status_code = response.status_code if 'response' in locals() else None
            if status_code == 429:
                print(f"Rate limit hit on attempt {attempt}. Retrying in {backoff} seconds...")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)  # backoff at 60 seconds
            else:
                print(f"OpenAI API error on attempt {attempt}: {e}")
                break
        except Exception as e:
            print(f"Unexpected error on attempt {attempt}: {e}")
            break
    return None

def post_to_x(message):
    
    # Ensure message length within X limit
    if len(message) > 280:
        message = message[:277] + "..."
    try:
        response = client.create_tweet(text=message)
        print(f"Successfully posted tweet ID: {response.data['id']}")
        return True
    except Exception as e:
        print(f"Error posting tweet: {e}")
        return False

if __name__ == "__main__":
    
    # Direct message example
    post_to_x("Cristiano Ronaldo is the greatest footballer(GOAT) of all time.")

    # AI-generated message example
    ai_prompt = "Generate a tweet about cristiano ronadlo being the greatest footballer of all time."
    generated_message = generate_ai_content(ai_prompt)
    if generated_message:
        post_to_x(generated_message)
    else:
        print("Failed to generate AI content.")