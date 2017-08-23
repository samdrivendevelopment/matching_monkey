
def should_quit(char):
    if char in ('q', 'quit'):
        return True
    return False

def is_invalid(char, len_board):
    if char not in len_board:
        return True
    return False

def is_overlapping(char_index, board):
    if board[char_index] != '_':
        return True
    return False

def has_matched(st, nd, state):
    if st == nd:
        return False
    if state['key'][st] == state['key'][nd]:
        return True
    return False

def flip_card(first, second, state):
        state['board'][first] = state['key'][first]
        state['board'][second] = state['key'][second]
        state['matches'] += 1

def has_won(board_list):
    for i in range(len(board_list)):
        if board_list[i] == '_':
            return False
    return True

class ShellUI(object):
    def read(self):
        return raw_input('->')

    def write(self, text):
        print text

class CardMatchingGame(object):
    def turn(self):
        self.ui.write('First of the set is?')

        self.ui.write(self.state['board'])

        first_raw = self.ui.read()

        if should_quit(first_raw):
            return True

        if is_invalid(first_raw, self.state['len_board']):
            self.ui.write('That is a invalid charater.')
            return False

        if is_overlapping(int(first_raw), self.state['board']):
            self.ui.write('Someone is already there.')
            return False

        self.ui.write(self.state['key'][int(first_raw)])

        self.ui.write('Second of the set is?')

        second_raw = self.ui.read()

        if should_quit(second_raw):
            return True

        if is_invalid(second_raw, self.state['len_board']):
            self.ui.write('Now, we go back to the beginning.')
            return False

        if is_overlapping(int(second_raw), self.state['board']):
            self.ui.write('Someone is already there.')
            return False

        if has_matched(int(first_raw), int(second_raw), self.state):
            flip_card(int(first_raw), int(second_raw), self.state)
            self.ui.write('Matches: ' + str(self.state['matches']))
            self.ui.write(self.state['board'])
        else:
            self.ui.write('That was not a match sadly.')

        if has_won(self.state['board']):
            self.ui.write('You have won.')
            return True
        return False

def main():
    state = {
        'board': ['_'] * 10,
        'len_board': [str(i) for i in range(10)],
        'key': ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e'],
        'matches': 0,
    }

    game = CardMatchingGame()
    game.state = state
    game.ui = ShellUI()


    for i in range(999):
        should_break = game.turn()
        if should_break:
            break

if __name__ == '__main__':
    main()

