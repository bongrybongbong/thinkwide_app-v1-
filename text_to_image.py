import os
from dotenv import load_dotenv
from data.pages_mt import page_data
from openai import OpenAI
import httpx

client = OpenAI(api_key='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')


def use_dalle(page_data):
    # Dictionary to store the images' URLs
    image_urls = {}

    for page_key, page_values in page_data.items():
        title = page_values['title']
        description = page_values['description']
        keywords = page_values['keywords']

        # Prepare the prompt
        separate = "'''"
        prompt = f""" Please provide an illustration representing {title}. This is an image that represents the conversation log.
In the conversation, they talked about {description}.
The text, separated by triple backquotes {separate}. The key words in the conversation are {', '.join(keywords)}.
Create a cute illustration that best represents the theme of the conversation.
"""
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            )
 
        
        # Assuming the response contains a URL to the created image
        image_url = response.data[0].url

        # Save the URL
        # image_urls[page_key] = image_url
    
    return image_urls
    # 환경 변수 로드 및 OpenAI API 키 설정


image_urls = use_dalle(page_data)
print(image_urls)