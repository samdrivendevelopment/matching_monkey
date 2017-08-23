
from better_card_match import should_quit

def test_should_quit():
    return False
    result = should_quit('q')
    return result == True

def test_should_not_quit():
    return False
    result = should_quit('w')
    return result == False

def main():

    print 'start test'

    

