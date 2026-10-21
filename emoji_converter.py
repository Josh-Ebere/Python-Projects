# The '.split' method is used to split a string into different groups.
# The value entered into the parenthesis is what the code uses to split.
# This returns a list of the broken string.

def emoji_coverter(message):

    words = message.split(' ')

    emojis = {
        ":)": "😊",
        ":(": "😟",
        ":D": "😄"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output


message = input(">> ")
print(emoji_coverter(message))
