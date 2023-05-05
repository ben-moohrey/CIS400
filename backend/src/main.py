"""main.py"""

import sys
from classes.TermProject import TermProject
from classes.GPT import GPT


def main(args):
    """
    Main function to run complete program
    """
    user = None
    prompt = None


    gpt = GPT()
    for i in range(1,len(args[1:])+1):

        # User
        if i == 1:  
            user = str(args[i])
            print("User:", user)

        # Prompt
        if i == 2:
            prompt = str(args[i])
            print("Prompt:", prompt)

    if (user is not None and prompt is not None):
        termProject = TermProject(user)
        tt = termProject.get_top_tweets()
        generated = gpt.generate_tweets(tt, prompt)
        for t in generated:
            print(t)
        
    
if __name__ == "__main__":
    main(sys.argv)
    
   