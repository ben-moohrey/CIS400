"""main.py"""

import sys
from classes.TermProject import TermProject
user = None
prompt = None

def main(args):
    """
    Main function to run complete program
    """
    global user
    global prompt
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
        for t in tt[0:10]:
            print(t['full_text'])
            print()
    
if __name__ == "__main__":
    main(sys.argv)
    
   