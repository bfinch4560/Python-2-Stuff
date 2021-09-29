pyg = 'ay'

original = raw_input('Enter a word:')

first_letter = original[0]
second_letter = original[1]
third_letter = original[2]

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word[1:len(word)] + first + pyg
  print new_word
else:
  print 'empty'
