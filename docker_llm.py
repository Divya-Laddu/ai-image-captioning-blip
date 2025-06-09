from openai import OpenAI
import os

client = OpenAI(
    base_url="http://host.docker.internal:12434/v1",
    api_key="docker",
)


completion = client.chat.completions.create(
    model="ai/smollm2",
    messages=[{"role": "system", "content": "You are a helpful assistant."}, 
              {"role": "user", "content": "Hello, how are you?"}]
)

print(completion.choices[0].message.content)
