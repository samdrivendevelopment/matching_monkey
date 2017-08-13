
from card_matching import should_quit, is_invalid, has_matched,\
    is_overlapping, has_won

class FakeUI(object):
    def write(self, text):
        pass

def test_should_quit():
    result = should_quit('q')
    return result == True

def test_should_not_quit():
    result = should_quit('w')
    return result == False

def test_is_valid():
    len_board = ('0', '1')
    result = is_invalid('1', len_board)
    return result == False

def test_is_invalid():
    board_list = ('0', '1')
    result = is_invalid('t', board_list)
    return result == True

def test_has_matched():
    board_list = ('a', 'a')
    result = has_matched('0', '1', board_list)
    return result == True

def test_has_not_matched():
    board_list = ('a', 'b')
    result = has_matched('0', '1', board_list)
    return result == False

def test_is_overlapping():
    board_list = ('a', '_')
    result = is_overlapping(0, board_list)
    return result == True

def test_is_not_overlapping():
    board_list = ('a', '_')
    result = is_overlapping(1, board_list)
    return result == False

def test_has_won():
    board_list = ['a', 'a']
    result = has_won(board_list)
    return result == True

def test_has_not_won():
    board_list = ['a', '_']
    result = has_won(board_list)
    return result == False

def main():

    print 'start test'

    if not test_should_quit():
        print 'Should_quit did not detect the quit.'

    if not test_should_not_quit():
        print 'Should_quit detected a quit when it was not there'

    if not test_is_valid():
        print 'Is_invalid did not detect a valid char.'

    if not test_is_invalid():
        print 'Is_invalid detected a invalid char wwhen there was none.'

    if not test_has_matched():
        print 'Has_matched did not detect the match.'

    if not test_has_not_matched():
        print 'Has_matched detected a match when there was none.'

    if not test_is_overlapping():
        print 'Is_overlapping did not detect the overlapping.'

    if not test_is_not_overlapping():
        print 'Is_overlapping detected a overlap when there was none.'

    if not test_has_won():
        print 'Has_won did not detect the win.'

    if not test_has_not_won():
        print 'Has_won detected a win when there was none.'

    print 'end test'


if __name__ == '__main__':
    main()

