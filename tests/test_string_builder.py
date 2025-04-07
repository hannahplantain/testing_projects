from lib.string_builder import *

#adding an empty string to the string builder

def test_add_empty_string():
    string = StringBuilder()
    assert string.output() == ""

#adding one word to the string

def test_add_word_to_string():
    string = StringBuilder()
    string.add("Hello")
    assert string.output() == "Hello"

#counting the string with one word    

def test_add_word_and_count_string():
    string = StringBuilder()
    string.add("Hello")
    assert string.size() == 5

#adding two words to the string    

def test_add_multiple_words_to_string():
    string = StringBuilder()
    string.add("Hello")
    string.add(" world!")
    assert string.output() == "Hello world!"

#adding multiple strings and adding those strings correctly

def test_add_multiple_words_to_string_and_count():
    string = StringBuilder()
    string.add("Hello")
    string.add(" world!")
    assert string.size() == 12
