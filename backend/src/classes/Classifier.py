from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

class Classifier:
    def __init__(self):
        self.model_name = "facebook/bart-large-mnli"


    def get_buzzwords(self, tweets_text, num_buzzwords = 4):
        # Combine the tweets into a single text
        text = " ".join(tweets_text)

        # Load the model and tokenizer
        model_name = "facebook/bart-large-mnli"
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Initialize the zero-shot classification pipeline
        classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

        # Define a list of possible style categories
        style_categories = ['Absurd', 'Accusatory', 'Acerbic', 'Admiring', 'Aggressive', 'Aggrieved', 'Ambivalent', 'Amused', 'Angry', 'Animated', 'Apathetic', 'Apologetic', 'Appreciative', 'Ardent', 'Arrogant', 'Assertive', 'Awestruck', 'Belligerent', 'Benevolent', 'Bitter', 'Callous', 'Candid', 'Caustic', 'Cautionary', 'Celebratory', 'Chatty', 'Colloquial', 'Comic', 'Compassionate', 'Complex', 'Compliant', 'Concerned', 'Conciliatory', 'Condescending', 'Confused', 'Contemptuous', 'Critical', 'Cruel', 'Curious', 'Cynical', 'Defensive', 'Defiant', 'Demeaning', 'Depressing', 'Derisive', 'Detached', 'Dignified', 'Diplomatic', 'Disapproving', 'Disheartening', 'Disparaging', 'Direct', 'Disappointed', 'Dispassionate', 'Distressing', 'Docile', 'Earnest', 'Egotistical', 'Empathetic', 'Encouraging', 'Enthusiastic', 'Evasive', 'Excited', 'Facetious', 'Farcical', 'Flippant', 'Forceful', 'Formal', 'Frank', 'Frustrated', 'Gentle', 'Ghoulish', 'Grim', 'Gullible', 'Hard', 'Humble', 'Humorous', 'Hypercritical', 'Impartial', 'Impassioned', 'Imploring', 'Impressionable', 'Inane', 'Incensed', 'Incredulous', 'Indignant', 'Informative', 'Inspirational', 'Intense', 'Intimate', 'Ironic', 'Irreverent', 'Jaded', 'Joyful', 'Judgmental', 'Laudatory', 'Light-Hearted', 'Loving', 'Macabre', 'Malicious', 'Mean-Spirited', 'Mocking', 'Mourning', 'Naïve', 'Narcissistic', 'Nasty', 'Negative', 'Nostalgic', 'Objective', 'Obsequious', 'Optimistic', 'Outraged', 'Outspoken', 'Pathetic', 'Patronising', 'Pensive', 'Persuasive', 'Pessimistic', 'Philosophical', 'Playful', 'Pragmatic', 'Pretentious', 'Regretful', 'Resentful', 'Resigned', 'Restrained', 'Reverent', 'Righteous', 'Satirical', 'Sarcastic', 'Scathing', 'Scornful', 'Sensationalistic', 'Sentimental', 'Sincere', 'Sceptical', 'Solemn', 'Subjective', 'Submissive', 'Sulking', 'Sympathetic', 'Thoughtful', 'Tolerant', 'Tragic', 'Unassuming', 'Uneasy', 'Urgent', 'Vindictive', 'Virtuous', 'Whimsical', 'Witty', 'Wonder', 'World-Weary', 'Worried', 'Wretched']
        # Perform zero-shot classification
        result = classifier(text, style_categories)

        # Extract the top 2 style categories
        top_categories = sorted(
                zip(result["labels"], result["scores"]), key=lambda x: -x[1]
            )[:num_buzzwords]
        return [category for category, _ in top_categories]


# print("Style Profile:", ", ".join(buzzwords))