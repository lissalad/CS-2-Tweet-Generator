
def histogram(source_text):
    text = open(source_text).read().split()
    unique_words = []

    # text -> list of words
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~…‘“”'''

    for word in text:
  
        # de-capitalize
        word = word.lower()

        # go through letters in word
        for letter in word:
            if letter in punc:

                # remove character if it's in punctuation list
                word = word.replace(letter, "")

        word_found = False
        for unique in unique_words:

          # check to see if word already in dictionary (as first item in own list)
            if unique[0]==word:

                # if so, add 1 to its count
                unique[1] += 1 

                word_found = True 
                break
        if not word_found:

          # otherwise add word with starting count of 1 (as second item in own list)
            unique_words.append([word,1])

    return unique_words

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    for w in histogram:
        if word.lower() == w[0]:
            return w[1]

# -------------- RUNS ------------------------ #
if __name__ == '__main__':
    test = histogram("./john_mulaney.txt")
    print(test[3])
    print(unique_words(test))
    # print(frequency("i", test))
    # print(test)

    