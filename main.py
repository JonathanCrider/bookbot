import sys

def main():
  default_path = "books/frankenstein.txt"
  path_to_file = sys.argv[1] if len(sys.argv) > 1 else default_path
  book_text = get_book_text(path_to_file)
  if book_text is None:
    return
  
  word_count = get_word_count(book_text)
  if word_count < 1:
    print(f"Nothing to report, {path_to_file} was empty")
    return
  
  character_count = get_character_count(book_text)

  book_report(word_count, character_count, path_to_file)


# HELPER FUNCTIONS

def get_book_text(path):
  """
  Reads text from file path.
  Returns contents as string, or None if no file found.
  """
  try:
    with open(path) as f:
      file_contents = f.read()
  except FileNotFoundError:
    print(f"--- Error ---\nNo file found at {path}. Please check the file and try again")
    return None

  return file_contents


def get_word_count(file):
  """
  Returns approximate number of words.
  Splits on space, so may be slightly inaccurate.
  """
  word_count = len(file.split())
  return word_count


def get_character_count(file):
  """
  Returns a dictionary of every character in the file.
  Key/value of character/count.
  """
  character_count = {}
  all_lower_case = file.lower()

  for char in all_lower_case:
    if char in character_count:
      character_count[char] += 1
    else:
      character_count[char] = 1

  return character_count


def book_report(word_count, character_count, path_to_file):
  """
  Returns a report of both total number of words and a count of each character of the alphabet.
  Case insensitive.
  """
  alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
  
  print(f"--- Begin report of {path_to_file} ---")
  print(f"{word_count} words found in the document\n")
  for char in sorted(character_count):
    if char in alphabet:
      print(f"The '{char}' character was found {character_count[char]} times")
  print("--- End report ---")


main()
