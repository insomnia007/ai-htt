# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:33:28 2024

@author: biuro
"""
import csv
import pandas as pd
from openai import OpenAI
client = OpenAI(api_key='')

# Create an empty list to store the responses
responses_list = []

# Open the CSV file
with open('imagined_news_headlines.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = pd.read_csv(file)
    
    # Iterate through each row in the CSV file
    for index, row in csv_reader.iterrows():
        # Assuming the user content is in the first column of each row
        user_content = row[0]


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with headline, write short summary based on title. Use your imagination."
    },
    {
      "role": "user",
      "content": user_content
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)


# Append each response along with the headline to the list
for choice in response.choices:
    responses_list.append((user_content, choice.message.content))

# Create a DataFrame from the list of responses
df = pd.DataFrame(responses_list, columns=['Headline', 'Response'])
for choice in response.choices:
    print(choice.message.content)
