import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def predict(weather):

    prompt = f"""
    Predict rainfall chance from this weather data.

    {weather}

    Give:
    1. Rain Probability
    2. Confidence
    3. Trading Decision
    """

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content