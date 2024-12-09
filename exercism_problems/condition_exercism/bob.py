"""
Introduction
Bob is a lackadaisical teenager. He likes to think that he's very cool. And he definitely doesn't get excited about things. That wouldn't be cool.

When people talk to him, his responses are pretty limited.

Instructions
Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

Bob only ever answers one of five things:

"Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
"Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
"Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
"Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
"Whatever." This is what he answers to anything else.
"""

def response(hey_bob):
    hey_bob = str(hey_bob)
    # string_space = hey_bob.isspace()
    string_upper = hey_bob.isupper()
    string_strip = hey_bob.strip()
    string_end = string_strip.endswith("?")
    if not string_strip:
        return "Fine. Be that way!"
    elif string_end and string_upper:
        return "Calm down, I know what I'm doing!"
    elif string_end:
        return "Sure."
    elif string_upper:
        return "Whoa, chill out!"
    else:
        return "Whatever."

    # if(len(string)==0 or string.isspace() ):
    #     return "Fine. Be that way!"
    # elif(string_strip[-1] == "?" and string.isupper()):
    #     return "Calm down, I know what I'm doing!"
    # elif(string_strip[-1]== "?"):
    #     return "Sure."
    # elif(string.isupper()) :
    #     return "Whoa, chill out!"
    # else:
    #     return "Whatever."

print("Response : ",response("Tom-ay-to, tom-aaaah-to.")) # "Whatever."
print("Response : ",response("WATCH OUT!")) # "Whoa, chill out!"
print("Response : ",response("You are, what, like 15?")) # "Sure."
print("Response : ",response("WHAT'S GOING ON?")) # "Calm down, I know what I'm doing!"
print("Response : ",response("")) # "Fine. Be that way!"
print("Response : ",response("\n\r \t")) # "Fine. Be that way!"