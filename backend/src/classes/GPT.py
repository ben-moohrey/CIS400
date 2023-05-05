import openai
import src.constants as constants
import functools as ft
import json
class GPT:
    def __init__(self, max_tweets = 10, system_message = None, model = "gpt-3.5-turbo"):
        openai.organization = constants.OPENAI_ORG
        openai.api_key = constants.OPENAI_API_KEY
        self.max_tweets = max_tweets


        if (system_message is None):
            self.system_message = """
            Generate 5 new tweets each separated by the string '1x7ab' that mimic the style and voice 
            of the ten tweets provided, but focus on the content of the prompt given below. 
            Remove any links or hashtags. DO NOT include the original prompt in your output.
            DO NOT number the tweets in the output. 
            """.strip()

            # self.system_message = """
            # You are an API that takes in a Prompt and Top_Tweets in JSON format. With these tweets you are to return 5 
            # new tweets that mimic the style and voice of the Top_Tweets provided but with
            # the content of the Prompt. You are to return the 5 and only 5 tweets seperated by '\n'
            # characters and not numbered. Remove any links or hashtags. DO NOT include the original prompt in your output.
            # DO NOT number the tweets in the output. 
            # """
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

        request = json.dumps({
            "Prompt": prompt,
            "Top_Tweets": tweet_text[:min(self.max_tweets,len(tweet_text))]
        })

        print(request)
        
        # Send a request to openai to generate the tweets
        reponse = openai.ChatCompletion.create(
            model = self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": text},
            ]
        )

        # Get the tweets from the openai response
        print(reponse["choices"][0]["message"]["content"])
        generated_tweets = reponse["choices"][0]["message"]["content"].split('1x7ab')

        # Remove possible empty strings and return
        return [t for t in generated_tweets if t != '']
            

