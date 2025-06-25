word1 = '\tпришел'
word2 = '\t\tувидел'
word3 = '\t\t\tпобедил'
word4 = '\xA4\xBA\xA4'  # https://www.ascii-code.com/
word5 = '\u261e'
# https://home.unicode.org/
print(word1, word2, word3, sep='\n', end='!\n')
print(word4)
print(word5, 'Концерт группы \"Кино\"')