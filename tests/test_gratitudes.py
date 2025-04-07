from lib.gratitudes import *

#test adding an empty gratitude to the list

def test_adding_empty_string_gratitude():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "


#test adding a string as a new gratitude to the list

def test_adding_a_string_gratitude():
    gratitude = Gratitudes()
    gratitude.add("my family")
    assert gratitude.format() == "Be grateful for: my family"

#test adding the same string twice as a gratitude to the list

# def test_adding_two_of_the_same_string_gratitude():
#     gratitude = Gratitudes()
#     gratitude.add("my family")
#     gratitude.add("my family")
#     assert gratitude.format() == "Be grateful for: my family"

#test adding multiple different strings to the list

def test_adding_multiple_unique_strings_gratitude():
    gratitude = Gratitudes()
    gratitude.add("my family")
    gratitude.add("sunshine")
    assert gratitude.format() == "Be grateful for: my family, sunshine"
