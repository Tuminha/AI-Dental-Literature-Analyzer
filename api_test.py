import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
import requests

# Unset any existing API keys
for key in ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'DEEPSEEK_API_KEY', 'OPENROUTER_API_KEY']:
    if key in os.environ:
        del os.environ[key]

# Load environment variables
load_dotenv(override=True)

# Debug print for all API keys
for key in ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'DEEPSEEK_API_KEY', 'OPENROUTER_API_KEY']:
    api_key = os.environ.get(key)
    if api_key:
        print(f"{key} loaded: {api_key[:5]}...{api_key[-5:]}")
    else:
        print(f"{key} not found in .env file")

def test_openai_api():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, are you working?"}
            ]
        )
        print("OpenAI API test: Success")
        print(f"Response: {completion.choices[0].message.content}")
    except Exception as e:
        print(f"OpenAI API test: Failed - {str(e)}")

def test_anthropic_api():
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    try:
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=300,
            messages=[
                {"role": "user", "content": "Hello, are you working?"}
            ]
        )
        print("Anthropic API test: Success")
        print(f"Response: {message.content}")
    except Exception as e:
        print(f"Anthropic API test: Failed - {str(e)}")

def test_deepseek_api():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    url = "https://api.deepseek.com/v1/chat/completions"
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "Hello, are you working?"}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("DeepSeek API test: Success")
        print(f"Response: {response.json()['choices'][0]['message']['content']}")
    except Exception as e:
        print(f"DeepSeek API test: Failed - {str(e)}")

def test_openrouter_api():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://your-site.com",  # Replace with your actual site
        "X-Title": "API Test"
    }
    url = "https://openrouter.ai/api/v1/chat/completions"
    data = {
        "model": "openai/gpt-4",  # Changed to GPT-4
        "messages": [{"role": "user", "content": "Hello, are you working?"}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("OpenRouter API test: Success")
        print(f"Response: {response.json()['choices'][0]['message']['content']}")
    except Exception as e:
        print(f"OpenRouter API test: Failed - {str(e)}")

if __name__ == "__main__":
    test_openai_api()
    print("\n" + "-"*50 + "\n")
    test_anthropic_api()
    print("\n" + "-"*50 + "\n")
    test_deepseek_api()
    print("\n" + "-"*50 + "\n")
    test_openrouter_api()
