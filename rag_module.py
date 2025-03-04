import openai
import time
import random

openai.api_key = "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"

def answer_query(query, context):
    """
    Uses OpenAI to answer the query based on the provided context, with rate limiting and error handling.
    """
    for attempt in range(3):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{context} User Question: {query}"}],
                max_tokens=150
            )
            return response.choices[0].message['content'].strip()
        except openai.error.RateLimitError:
            print("Rate limit reached. Retrying...")
            time.sleep(5 + random.uniform(0, 5))  # Wait and retry with some randomness
        except openai.error.OpenAIError as e:
            print(f"OpenAI API error: {e}")
            time.sleep(5)
    return "Unable to retrieve answer at this time. Please try again later."