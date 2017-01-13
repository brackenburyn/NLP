# eliza2.py
# Written by Alex Mathson and Noah Brackenbury, expanded by Noah Brackenbury
# CS 322, Fall 2015
# This program simulates a conversation with a therapist (Eliza), using
# matching and substitution of regular expressions.  

import re
import sys


def main():
    print ("Hello. Please tell me about your problems.")
    while 'true':
    # The input is run through these regular expression substitutions
    # and then outputted in a different way in order to continue the
    # conversation
        message = input("").lower() 
        message = re.sub('^yes[\.!]?$', 'I see.', message)
        message = re.sub('^no[\.!]?$', 'Why not?', message)
        message = re.sub('^goodbye[\.!]?', 'Goodbye!', message)
        message = re.sub('.+ you[\.!\?]?$', \
                         "Let's not talk about me.", message)
        message = re.sub('^(.*) me (.*[\.\?!]?)$', r'\1 you \2', message)
        message = re.sub('^(.*) my (.*[\.\?!]?)$', r'\1 your \2', message)
        message = re.sub('^(.*) me[\.\?!]?$', r'\1 you.', message)
        message = re.sub('^what is (.+)\?$', \
                         r'Why do you ask about \1?', message)
        message = re.sub('^i am ([^\.!]+)[\.!]?$', \
                         r'Do you enjoy being \1?', message)
        message = re.sub('^why is (.+)\?$', \
                         r'Why do you think \1?', message)
        message = re.sub('^my ([^\.!\?]+)[\.!\?]?$', r'Your \1?', message)
        message = re.sub('^(.+) hurts?[\.!\?]?$', \
                         r"\1 is just physical. How does it make you feel?",\
                         message)
        message = re.sub('^can you ([^\.\?!]+)[\?\.!]?$', \
                         r"I'm sorry, I'm afraid I can't \1.", message)
        message = re.sub("^(.+) doesn't ([^\.!\?]+)[\.!\?]?$", \
                         r"Why doesn't \1 \2?", message)
        message = re.sub('^i hate ([^\.\?!]+)[\.\?!]?$', \
                         r'Really? I rather like \1. Your loss.', message)
        message = re.sub('^i dislike ([^\.\?!]+)[\.\?!]?$', \
                         r'Really? I rather like \1. Your loss.', message)
        message = re.sub("^i don'?t like ([^\.\?!]+)[\.\?!]?$", \
                         r'Really? I rather like \1. Your loss.', message)
        message = re.sub('^i like ([^\.\?!]+)[\.\?!]?$', \
                         r'Then surround your life with \1.', message)
        message = re.sub('^i love ([^\.\?!]+)[\.\?!]?$', \
                         r'Then surround your life with \1.', message)
        message = re.sub("^([^\.\?!]+) is difficult[\.\?!]?$", \
                         r"You will feel much better once you've done \1.",\
                         message)
        message = re.sub("^is difficult[\.\?!]?$", \
                         r"You will feel much better once you've done \1.",\
                         message)
        message = re.sub('^([^\.\?!]+) dislikes me[\.\?!]?', \
                         r'I think that \1 is entitled to their opinion.', \
                         message)
        message = re.sub('^.+ broke up with .+[\.\?!]?$', \
                         r'How do you feel about this?', message)
        message = re.sub('^.+ dumped .+[\.\?!]?$', \
                         r'How do you feel about this?', message)
        message = re.sub('^.* bad .*[\.\?!]?$', \
                         r'Bad in what way?', message)
        # Replaces any unmodified message with the base case 
        # response, "Please go on".
        message = re.sub('^[^A-Z]*$', 'Please go on.', message)
        print(message)
        if message == 'Goodbye!':
        # Exits the program when the user types "goodbye"
            sys.exit()

if __name__ == '__main__':
    main()
