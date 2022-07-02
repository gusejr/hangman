import random

new_word = open('new_word.txt', 'r')
random_word = random.choice(new_word.readlines()).splitlines()[0]
# print(random_word)
