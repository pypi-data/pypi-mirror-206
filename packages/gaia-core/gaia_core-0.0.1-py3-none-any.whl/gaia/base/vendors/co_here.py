import os
import cohere

class CoHereService:
    name = 'CoHere'
    co = None
    def __init__(self, api_key=None):
        key = api_key
        self.co = cohere.Client(key)
    # @staticmethod
    # def run_chat(prompt, stream=False, temperature=0, role='user', model='gpt-3.5-turbo'):
    #     response = openai.ChatCompletion.create(
    #         model=model,
    #         messages=[
    #             {
    #                 'role': role,
    #                 'content': prompt
    #             }
    #         ],
    #         temperature=temperature,
    #         stream=stream
    #     )
    #     return response

    def run_completion(self, prompt, max_tokens, stream=False, temperature=0.9, model='command-xlarge-nightly'):
        prediction = self.co.generate(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            stream=stream,
            temperature=temperature,
            k=0,
            p=0.75,
            return_likelihoods="NONE",
            stop_sequences=[]
            # frequency_penalty=0.1,
            # presence_penalty=0,
            # stop_sequences=["--"]
        )
        return prediction

    def get_tokens(self, prompt):
        response = self.co.tokenize(
            text=prompt,
        )
        tokens = response.tokens
        token_strings = response.token_strings
        num_tokens = len(tokens)
        return num_tokens

    def get_price(self, tokens):
        price = tokens * (2.5/1000)
        return price
    def calculate_price(self, prompt):
        num_tokens = self.get_tokens(prompt)
        return self.get_price(num_tokens)
    def calc_tokens(self):
        response = self.co.tokenize(
            text='tokenize me! :D',
        )
