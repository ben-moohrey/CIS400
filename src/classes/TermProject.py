"""
TermProject.py

Class contains the logic to scrape the followers from a specific user and return 5
tweets that are in the style
"""
import modules.TwitterTools as tt
import constants

class TermProject:
    def __init__(self, user):
        self.user = user
        self.twitter_api = tt.oauth_login(
            constants. OAUTH_TOKEN,
            constants.OAUTH_TOKEN_SECRET,
            constants.CONSUMER_KEY,
            constants.CONSUMER_SECRET,
        )

    def get_top_tweets(self, name=None):
        if name is None:
            name = self.user
        tweets = tt.harvest_user_timeline(
            self.twitter_api,
            screen_name=name,
            max_results=2000
        )
        return tt.find_popular_tweets(tweets)
        

