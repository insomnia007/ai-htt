# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:40:52 2024

@author: biuro
"""

from openai import OpenAI
client = OpenAI(api_key='')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."
    },
    {
      "role": "user",
      "content": "Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."
    }
  ],
  temperature=0.5,
  max_tokens=64,
  top_p=1
)
print(response.choices[0].message.content)

import pandas as pd

# Extract keywords from completion response
keywords = response.choices[0].message.content.strip().split(", ")

# Create a dataframe with the keywords
df = pd.DataFrame({"Keywords": keywords})

# Display the dataframe
print(df)