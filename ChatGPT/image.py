import os
import openai

openai.api_key = os.getenv("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")
response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']