import random

def histogram(source_text):
  punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~…‘“”'''
  words = {}
  text = open(source_text).read().split() # text -> list of words

  for w in text:
    w = w.lower() # de-capitalize
    for letter in w: # go through letters in word
      if letter in punc: 
        w = w.replace(letter, "") # remove character if it's in punctuation list

    if w in words.keys(): # check to see if word already in dictionary
      words[w] += 1 # if so, add 1 to its count 
    else:
      words[w] = 1 # otherwise add word with starting count of 1
  return words

def unique_words(histogram): # number of unique words in histogram
  return len(histogram)

def frequency(word, histogram): # how many times a word appears in a histogram
  return histogram.get(word.lower())

def randomWord(histogram): # random word, does consider distribution
  total_words = []
  for item in histogram.keys():
    for count in range(histogram.get(item)):
      total_words.append(item)
  word =  total_words[random.randrange(0, len(total_words)-1)]
  return word

def randWord(histogram):
  words = []
  count = []


# -------------- RUNS ------------------------ #
if __name__ == '__main__':
    test = histogram("./john_mulaney.txt")
    # print(unique_words(test))
    # print(frequency("john", test))
    print(randomWord(test))

