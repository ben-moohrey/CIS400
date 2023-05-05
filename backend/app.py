from flask import Flask, request ,jsonify
from flask_cors import CORS
from src.classes.TermProject import TermProject
from src.classes.GPT import GPT
from src.classes.Classifier import Classifier

TOP_X = 10

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Allow CORS only for specific origin
gpt = GPT()
termProject = TermProject()
classifier = Classifier()


@app.route('/api/analyze', methods=['POST'])
def get_data():
    data = request.json
    twitter_handle = data['twitter_handle']
    prompt = data['prompt']

    # Call Tweet Analyzer function with the user's input, and get the results.
    tt = termProject.get_top_tweets(twitter_handle)
    generated = gpt.generate_tweets(tt, prompt)

    
   
    return jsonify({
        "results": generated,
    })

@app.route('/api/buzzwords', methods=['POST'])
def analyze():
    data = request.json
    twitter_handle = data['twitter_handle']

    # Call Tweet Analyzer function with the user's input, and get the results.
    tt = termProject.get_top_tweets(twitter_handle)
    tweet_text = list(map(lambda t: t['full_text'], tt))[:min(TOP_X,len(tt))]
    buzzwords = classifier.get_buzzwords(tweets_text=tweet_text)
   
    return jsonify({
        "buzzwords": buzzwords
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
