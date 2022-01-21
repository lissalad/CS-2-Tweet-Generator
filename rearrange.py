import sys
import random

def rearrange(words):
    random.shuffle(words)
    return words

if __name__ == "__main__":
    print(rearrange(sys.argv[1:]))