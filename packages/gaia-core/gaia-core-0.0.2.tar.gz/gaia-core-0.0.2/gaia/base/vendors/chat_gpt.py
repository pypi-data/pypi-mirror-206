import os
import openai
import requests
import json
import tiktoken

class ChatGptService:
    name = 'ChatGpt'
    api_key = None
    def __init__(self, api_key=None):
        self.api_key = api_key

    def run_chat(self, prompt, history=[], stream=False, temperature=0, role='user', model='gpt-3.5-turbo'):
        message = [
            {
                'role': role,
                'content': prompt
            }
        ]
        messages = history + message
        response = openai.ChatCompletion.create(
            api_key=self.api_key,
            model=model,
            messages=messages,
            temperature=temperature,
            stream=stream
        )
        return response

    def run_completion(self, prompt, max_tokens, stream=False, temperature=0, engine="text-davinci-003"):
        completion = openai.Completion.create(
            api_key=self.api_key,
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            n=1,
            stream=stream
        )
        return completion

    def get_tokens(self, prompt):
        enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokens = enc.encode(prompt)
        num_tokens = len(tokens)
        return num_tokens

    def get_price(self, tokens):
        price = tokens * (0.002 / 1000)
        return price
    def calculate_price(self, prompt):
        num_tokens = self.get_tokens(prompt)
        return self.get_price(num_tokens)

    def get_price2(self, prompt, model="gpt-3.5-turbo"):
        """Returns the number of tokens used by a list of messages."""
        messages = [prompt]
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo":  # note: future models may deviate from this
            num_tokens = 0
            for message in messages:
                num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":  # if there's a name, the role is omitted
                        num_tokens += -1  # role is always required and always 1 token
            num_tokens += 2  # every reply is primed with <im_start>assistant
            print('num_tokens', num_tokens)
            price = num_tokens * (0.002 / 1000)
            return price
        else:
            raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
    See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tok""")