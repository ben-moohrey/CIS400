import openai
import constants
import functools as ft
class GPT:
    def __init__(self, max_tweets = 10, system_message = None, model = "gpt-3.5-turbo"):
        openai.organization = constants.OPENAI_ORG
        openai.api_key = constants.OPENAI_API_KEY
        self.max_tweets = max_tweets


        if (system_message is None):
            self.system_message = """
            Based on the following tweets and prompt, give me 
            5 tweets separated by newlines in the same style and 
            voice of the the 10 tweets but with the content of the prompt. 
            Don't return anything else. Only return the 5 tweets. 
            Make sure that the original prompt is not included.
            """.strip()
        else:
            self.system_message = system_message

        self.model = model


    def generate_tweets(self, user_tweets, prompt):
        tweet_text = list(map(lambda t: t['full_text'], user_tweets)) 

        # Format the request
        text = "Prompt:\n{0}\n\nTweets:\n{1}".format(prompt,str(ft.reduce(
            lambda x, y: x + '\n\n' + y,
            tweet_text[:min(self.max_tweets,len(tweet_text))] 
        )))
        
        # Send a request to openai to generate the tweets
        reponse = openai.ChatCompletion.create(
            model = self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": text},
            ]
        )

        # Get the tweets from the openai response
        generated_tweets = reponse["choices"][0]["message"]["content"].split('\n')

        # Remove possible empty strings and return
        return [t for t in generated_tweets if t != '']
            

