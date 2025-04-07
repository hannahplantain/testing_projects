from lib.counter import *

#testing without adding anything to the counter

def test_counter_0():
    counter = Counter()
    assert counter.report() =="Counted to 0 so far."

#testing adding 10 to the counter

def test_counter_10():
    counter = Counter()
    counter.add(10)
    assert counter.report() == "Counted to 10 so far."

#testing when two numbers are added, they should be counted and added together

def test_counter_adds_multiple_numbers():
    counter = Counter()
    counter.add(15)
    counter.add(5)
    assert counter.report() == "Counted to 20 so far."


#testing the result of adding two numbers with one being negative

def test_counter_adds_negative_and_positive():
    counter = Counter()
    counter.add(15)
    counter.add(-5)
    assert counter.report() == "Counted to 10 so far."

def test_counter_adds_negative_and_positive_ends_negative():
    counter = Counter()
    counter.add(5)
    counter.add(-20)
    assert counter.report() == "Counted to -15 so far."