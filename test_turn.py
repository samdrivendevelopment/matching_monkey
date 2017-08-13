
from card_matching import CardMatchingGame

class BetterTestUI(object):
    def read(self):
        fake_user_input = self.input_list[self.index]
        self.index += 1
        return fake_user_input

    def write(self, text):
        pass

def make_better_test_game(input_list):
    state = {
        'board': ['_', '_', '_', '_'],
        'len_board': ['0', '1', '2', '3'],
        'key': ['a', 'a', 'b', 'b'],
        'matches': 0,
    }
    game = CardMatchingGame()
    game.state = state
    game.ui = BetterTestUI()
    game.ui.index = 0
    game.ui.input_list = input_list
    return game

def test_should_st_quit():
    game = make_better_test_game(['q'])
    result = game.turn()
    return result == True

def test_should_st_not_quit():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    return result == False

def test_should_nd_quit():
    game = make_better_test_game(['1', 'q'])
    result = game.turn()
    return result == True

def test_should_nd_not_quit():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    return result == False

def test_is_st_valid():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    same_board = game.state['board'] == ['_', '_', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_is_st_invalid():
    game = make_better_test_game(['t'])
    result = game.turn()
    same_board = game.state['board'] == ['_', '_', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_is_nd_valid():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    same_board = game.state['board'] == ['_', '_', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_is_nd_invalid():
    game = make_better_test_game(['1', 't'])
    result = game.turn()
    return result == False
    same_board = game.state['board'] == ['_', '_', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_is_st_overlapping():
    game = make_better_test_game(['1'])
    game.state['board'][1] = 'a'
    result = game.turn()
    same_board = game.state['board'] == ['_', 'a', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_is_st_not_overlapping():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    same_board = game.state['board'] == ['_', '_', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_is_nd_overlapping():
    game = make_better_test_game(['1', '2'])
    game.state['board'][2] = 'b' 
    result = game.turn()
    same_board = game.state['board'] == ['_', '_', 'b', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_is_nd_not_overlapping():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    same_board = game.state['board'] == ['_', '_', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_reset():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    same_board = game.state['board'] == ['_', '_', '_', '_']
    same_matches = game.state['matches'] == 0
    return (result == False) and same_board and same_matches

def test_match():
    game = make_better_test_game(['0', '1'])
    result = game.turn()
    board_change = game.state['board'] == ['a', 'a', '_', '_']
    matches_change = game.state['matches'] == 1
    return (result == False) and board_change and matches_change

def test_has_won():
    game = make_better_test_game(['0', '1'])
    game.state['board'] = ['_', '_', 'b', 'b']
    result = game.turn()
    return result == True

def test_has_not_won():
    game = make_better_test_game(['1', '2'])
    result = game.turn()
    return result == False

def main():

    print 'start test'

    if not test_should_st_quit():
        print 'turn did not detect the first quit.'

    if not test_should_st_not_quit():
        print 'turn detected a first quit when there was none.'

    if not test_should_nd_quit():
        print 'turn did not detect the secondquit.'

    if not test_should_nd_not_quit():
        print 'turn detected a second quit when there was none.'

    if not test_is_st_valid():
        print 'turn detected a first invalid char when there was none.'

    if not test_is_st_invalid():
        print 'turn did not detect the first invaild char.'

    if not test_is_nd_valid():
        print 'turn detected a second invalid char when there was none.'

    if not test_is_nd_invalid():
        print 'turn did not detect the second invalid char.'

    if not test_is_st_overlapping():
        print 'turn did not detect the first overlap.'

    if not test_is_st_not_overlapping():
        print 'turn detected a first overlap when there was none.'

    if not test_is_nd_overlapping():
        print 'turn did not detect the second overlap.'

    if not test_is_nd_not_overlapping():
        print 'turn detected a second overlap when there was none.'

    if not test_reset():
        print 'turn did not detect the reset.'

    if not test_match():
        print 'turn did not detect the match.'

    if not test_has_won():
        print 'turn did not detect the win.'

    if not test_has_not_won():
        print 'turn detected a win when there was none.'

    print 'end test'

if __name__ == '__main__':
    main()

