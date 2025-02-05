# BookBot

First Python project. Reinforcing the concepts explored in the [boot.dev](https://www.boot.dev/) Python course, and learing a few new ones (tests!)

BookBot allows you to process text files and generate reports on word and character usage.

## Installation

Ensure you have Python installed on your system. Clone the repository, and navigate to the project directory:

```bash
git clone https://github.com/JonathanCrider/bookbot.git && cd $_
```

## Usage

To run the project using a custom file path (only txt files officially supported):

```bash
python main.py <path/to/file.txt>
```

Example:

```bash
python main.py books/my_book.txt
```

**Note:** If no file path is included, the default included Frankenstein text will be used:

```bash
python main.py
```

## Tests

To run the tests:

```bash
python run-tests.py
```
