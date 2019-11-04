phrase = "The right format"

# life = 42
# while life - len(phrase) - 1:
#     life -= 1
#     print('-', end = '')
# print(phrase)
# print("{:->42}".format(phrase))

print(phrase.rjust(42, '-'))
