# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# I speak text message 2007 j1

# OVER COMPLICATED THE PROBLEM!

translation = {
    "CU": "see you",
    ":-)": "I'm happy",
    ":-(": "I'm unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you're welcome",
    "TTYL": "talk to you later"
}

while True:
    text = input()

    text_list = text.split()

    translated_sentece = ""

    for word in text_list:
        if (word in translation):
            translated_sentece = translated_sentece + " " + translation[word]
        else:
            translated_sentece = translated_sentece + " " + word
    print(translated_sentece)

    if (text == "TTYL"):
        break
