# pig.py
#
# A231 Python 2 Spring 2021
# Credit: Van Nguyen, C02699930
# HW01: Implement the game of Pig.
#
# I appended "_" to each class attribute to indicate internal use only.
# Not sure if that is the standard in Python.
# Are we supposed to provide the type for "self"?



import random
import sys



INDENT = ' ' * 5
BORDER = '.' * 20

# Weights chosen semi-arbitrarily. The pigs will be most likely be
# touching, sometimes touch, and very rarely piggyback.
# Index 0: Not Touching
# Index 1: Oinker - Reset to 0
# Index 2: Piggyback - Instant Lose
TOUCH_WEIGHTS = (80, 19, 1)

# Weights chosen by adding 13 to each score. As a result, the 
# converted scores add up to 100.
# Index 0: Sider - 0 pts
# Index 1: Razorback - 5 pts
# Index 2: Trotter - 5 pts
# Index 3: Snouter - 10 pts
# Index 4: Leaning Jowler - 15 pts
ROLL_WEIGHTS = (13, 18, 18, 23, 28)
ROLL_TYPES = (
    ('Sider', 0),
    ('Razorback', 5),
    ('Trotter', 5),
    ('Snouter', 10),
    ('Leaning Jowler', 15),
)


def printInd(text: str) -> None:
    'Adds an indentation before printing the text.'

    print(INDENT + text)



class pig():
    '''
    Runs a command line game of pig for two players.
    Players take turns choosing to pass or roll. 
    Rolls have a weighted chance of getting different results.
    The game ends if a player wins by hitting the target score or 
    loses by rolling a "piggyback".
    '''


    def _print_score(self) -> None:
        'Prints the score of the players.'

        print(f'{self._players[0]["name"]}: {self._players[0]["score"]}, '
            f'{self._players[1]["name"]}: {self._players[1]["score"]}')


    def _indiv_roll(self) -> int:
        '''Randomly chooses a value from 0 - 4 based on the defined 
        weights.'''

        return random.choices(range(5), weights=ROLL_WEIGHTS)[0]

    
    def _next_player(self) -> None:
        '''
        Flips the _player_state from 0 to 1 and vice-versa.
        If both players have lost, it ends the game.
        '''

        if (self._players[0]['score'] == 'LOST' and 
            self._players[1]['score'] == 'LOST'):
            self._game_active = False
        elif self._players[0]['score'] == 'LOST':
            self._player_state = 1
        elif self._players[1]['score'] == 'LOST':
            self._player_state = 0
        else:
            self._player_state = 1 if self._player_state == 0 else 0


    def __init__(self, player_1: str, player_2: str, win_score: int) -> None:
        'Initiates class attributes and starts the game.'

        self._win_score = int(win_score)
        self._game_active = True
        self._player_state = 0
        self._players = [
            {
                'name': player_1,
                'score': 0,
            },
            {
                'name': player_2,
                'score': 0,
            },
        ]

        self._start_game()


    def _start_game(self) -> None: 
        'Starts the game. Endlessly loops until the game ends.'

        print(f'Competitors: {self._players[0]["name"]}' 
              f' vs {self._players[1]["name"]}\n')
        
        while self._game_active:
            print(BORDER)
            self._print_score()
            print(BORDER)
            
            self._start_turn()

        self._end_game()


    def _start_turn(self) -> None:
        'Starts a turn. Endlessly loops until the turn ends.'

        print(f'Your turn, {self._players[self._player_state]["name"]}\n')

        turn_active = True

        while turn_active:
            turn_choice = input(INDENT + 'ROLL or PASS? ').lower()
            
            if turn_choice == 'roll':
                turn_active = self._roll_choice()
            elif turn_choice == 'pass':
                turn_active = self._pass_choice()

    
    def _roll_choice(self) -> bool:
        '''
        Executes the logic for a roll and updates the player score
        accordingly. Returns a bool value whether or not the turn is
        still active.
        '''

        touch_result = random.choices(
            range(3), 
            weights=TOUCH_WEIGHTS)[0]

        if touch_result == 0:
            # Not Touching Roll
            roll_1 = self._indiv_roll()
            roll_2 = self._indiv_roll()

            pointsEarned = (ROLL_TYPES[roll_1][1] 
                        + ROLL_TYPES[roll_2][1])
            self._players[self._player_state]["score"] += pointsEarned

            if roll_1 == roll_2:
                # Rolled a Double
                printInd(
                    f'You rolled a Double {ROLL_TYPES[roll_1][0]}')
                printInd(f'You earned {pointsEarned} points\n')
            else:
                # Rolled a Mixed Combo
                printInd('You rolled a Mixed Combo: '
                    f'{ROLL_TYPES[roll_1][0]} and '
                    f'{ROLL_TYPES[roll_2][0]}')
                printInd(f'You earned {pointsEarned} points\n')
            
            return True

        elif touch_result == 1:
            # Oinker Roll
            self._players[self._player_state]["score"] = 0

            printInd('You rolled an Oinker!')
            printInd('You lose all your points')

            self._next_player()
            return False

        elif touch_result == 2:
            # Piggyback Roll
            self._players[self._player_state]["score"] = 'LOST'

            printInd('You rolled a Piggyback!')
            printInd('You are out of the game')

            self._next_player()
            return False

    
    def _pass_choice(self) -> bool:
        '''
        Executes the logic for a pass. Checks whether or not if the
        current player has won. Always returns a bool value of False
        indicating that the turn is no longer active.
        '''

        if (self._players[self._player_state]["score"] >= self._win_score):
            self._game_active = False
        else:
            self._next_player()
        
        return False


    def _end_game(self) -> None:
        'Prints the end score and the winner of the game.'

        print('\n\n' + BORDER)
        print('GAME OVER')
        self._print_score()
        
        winner_exists = False

        for player in self._players:
            if player['score'] == 'LOST':
                continue
            elif player['score'] >= self._win_score:
                winner_exists = True
                print(f'{player["name"]} wins!')
                break
        
        if not winner_exists:
            print('No one wins.')



pig(sys.argv[1], sys.argv[2], sys.argv[3])


