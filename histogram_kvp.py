
def histogram(source_text):
  punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~…‘“”'''
  words = {}
  text = open(source_text).read().split()
  for w in text:
    w = w.lower()
    for letter in w:
      if letter in punc:
        w = w.replace(letter, "")
    if w in words.keys():
      words[w] += 1
    else:
      words[w] = 1
  # print(len(words))
  # print(words)
  return words

def unique_words(histogram):
  return len(histogram)

def frequency(word, histogram):
  return histogram.get(word)

if __name__ == '__main__':
    test = histogram("./john_mulaney.txt")
    print(unique_words(test))
    print(frequency("john", test))