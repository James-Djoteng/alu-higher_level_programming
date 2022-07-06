#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}","Last 2 letters: {word_last_2}","Middle word: {middle_word}")
