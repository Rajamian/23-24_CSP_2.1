# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(passwords):
  words = get_dictionary()
  guesses = 0
  for w1 in words:
    for w2 in words:
      phrase = w1 + w2
    guesses = guesses + 1
    if phrase == passwords:
      guesses += 1
      return True, guesses
  return False, guesses
