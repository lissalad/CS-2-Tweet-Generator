import random
import sys

def random_words(count):
    words = random.choices(open("/usr/share/dict/words").read().split(), k=count)
    for i in words:
        println(i + " ")

if __name__ == "__main__":
    random_words(int(sys.argv[1]))

