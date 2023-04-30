import openai
import os

# Set up API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the prompt for the AI to complete
prompt = "What is the meaning of life?"

# Define the parameters for the AI to use
model = "text-davinci-002"
temperature = 0.5
max_tokens = 50

# Call the OpenAI API to generate text
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Print the generated text
print(response.choices[0].text.strip())