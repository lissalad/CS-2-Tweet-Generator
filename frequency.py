
def histogram(source_text):
    text = open(source_text).read().split()
    # print(text)
    # print(len(text))
    unique_words = []
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~…‘“”'''
    for word in text:
        word = word.lower()
        for letter in word:
            if letter in punc:
                word = word.replace(letter, "")
        word_found = False
        for unique in unique_words:
            if unique[0]==word:
                unique[1] += 1
                word_found = True
                break
        if not word_found:
            unique_words.append([word,1])
    return unique_words

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    for w in histogram:
        if word.lower() == w[0]:
            return w[1]

if __name__ == '__main__':
    test = histogram("./john_mulaney.txt")
    print(test[3])
    print(unique_words(test))
    # print(frequency("i", test))
    # print(test)