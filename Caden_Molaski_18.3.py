import random
def random_format(words):
    alignments = [">", "<", "^"]
    for word in words:
        alignment = random.choice(alignments)
        width = random.randint(len(word) + 1, len(word) + 10)
        format_string = f"{{:{alignment}{width}}}"
        print(format_string.format(word))

#main
words = ["this", "is", "my", "favorite", "codelike", "problem", "possibly", "ever"]


random_format(words)