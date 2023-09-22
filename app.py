import os
import openai
from dotenv import load_dotenv
load_dotenv('.env')

# Access configuration settings
api_key = os.environ.get('API_KEY')

# Read conversation data from a text file
def read_conversation_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Cleaned conversation data with roles
file_path = 'output.txt'
conversation_lines = read_conversation_file(file_path)

# Convert lines to a list of dictionaries with roles
conversation = []
for line in conversation_lines:
    role, content = line.split(': ', 1)
    if role=='Jeevitha':
        role = 'user'
    else:
        role = 'system'
    message = {"role": role, "content": content}
    conversation.append(message)

conversation = conversation[:100]
# Generate a response using GPT-3
def generate_response(messages):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=1024
    )
    return response['choices'][0]['message']['content']

# Extend the conversation with a new message from Jeevitha(ITC)
new_message = {"role": "user", "content": "we hv to do everything as it is like in ex2"}
conversation.append(new_message)

# Generate a response based on the extended conversation
response = generate_response(conversation)
print(response)