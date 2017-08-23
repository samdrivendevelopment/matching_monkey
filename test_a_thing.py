
from card_matching import should_quit, is_invalid, has_matched,\
    is_overlapping, has_won, flip_card

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
    board_list = (0, 1)
    result = is_invalid('t', board_list)
    return result == True

def test_has_matched():
    state = {
        'board': ['_', '_', '_', '_'],
        'len_board': ['0', '1', '2', '3'],
        'key': ['a', 'a', 'b', 'b'],
        'matches': 0,
    }
    result = has_matched(0, 1, state)
    return result == True

def test_has_not_matched():
    state = {
        'board': ['_', '_', '_', '_'],
        'len_board': ['0', '1', '2', '3'],
        'key': ['a', 'a', 'b', 'b'],
        'matches': 0,
    }
    result = has_matched(0, 2, state)
    return result == False

def test_flip_card():
    first = 0
    second = 1
    state = {
        'board': ['_', '_', '_', '_'],
        'len_board': ['0', '1', '2', '3'],
        'key': ['a', 'a', 'b', 'b'],
        'matches': 0,
    }
    flip_card(first, second, state)
    good_board = ['a', 'a', '_', '_']
    matches = 1
    return state['board'] == good_board, state['matches'] == matches

def test_not_flip():
    first = 0
    second = 2
    state = {
        'board': ['_', '_', '_', '_'],
        'len_board': ['0', '1', '2', '3'],
        'key': ['a', 'a', 'b', 'b'],
        'matches': 0,
    }
    flip_card(first, second, state)
    good_board = ['_', '_', '_', '_']
    matches = 0
    return state['board'] == good_board, state['matches'] == matches


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

    if not test_flip_card():
        print 'Flip_card did not flip card when it should have.'

    if not test_not_flip():
        print 'Flip_card flipped a card when it should not have.'

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

