# The problem the dataset given has both words and sentences, so it's hard especially for sentences

# use the cleaned up file, prefers that, easier
bad_words_file = "./bad_words.txt"

# debug toggle
debug = False

# open bad word list
with open(bad_words_file) as f:
    bad_words = []

    for word in f:
        bad_words.append(word.strip())

    if debug:
        print(bad_words)

if __name__ == "__main__":
    # supposed good words
    # words = ["hello", "bye", "goodbye", "fuckers", "asshole"]
    #
    # for word in words:
    #     if word in bad_words:
    #         print(word, "is not allowed")

    # while true of user input
    while True:
        word = input("Enter a word: ")
        if word in bad_words:
            print(" Sorry the word is not allowed")
