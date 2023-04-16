"""main.py"""

import sys



user = ""
prompt = ""

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


    


if __name__ == "__main__":

    main(sys.argv)