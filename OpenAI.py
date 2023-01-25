import openai
import os


class OpenAI:

    def __init__(self):
        OpemAiToken = os.environ.get('opemAItokem')
        openai.api_key = OpemAiToken

    def GetData(self, texto):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=texto,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5
        )
        return response["choices"][0]["text"]
