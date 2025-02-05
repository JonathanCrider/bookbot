def main():
  path_to_file = "books/frankensteins.txt"
  book_text = get_book_text(path_to_file)
  if book_text is None:
    return
  
  word_count = get_word_count(book_text)
  if word_count < 1:
    print(f"Nothing to report, {path_to_file} was empty")
    return
  
  character_count = get_character_count(book_text)

  book_report(word_count, character_count, path_to_file)


def get_book_text(path):
  try:
    with open(path) as f:
      file_contents = f.read()
  except FileNotFoundError:
    print(f"--- Error ---\nNo file found at {path}. Please check the file and try again")
    return None

  return file_contents


def get_word_count(file):
  word_count = len(file.split())
  return word_count


def get_character_count(file):
  character_count = {}
  all_lower_case = file.lower()

  for char in all_lower_case:
    if char in character_count:
      character_count[char] += 1
    else:
      character_count[char] = 1

  return character_count


def book_report(word_count, character_count, path_to_file):
  alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
  
  print(f"--- Begin report of {path_to_file} ---")
  print(f"{word_count} words found in the document\n")
  for char in sorted(character_count):
    if char in alphabet:
      print(f"The '{char}' character was found {character_count[char]} times")
  print("--- End report ---")


main()
