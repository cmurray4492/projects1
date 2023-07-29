"""Rock Paper Scissors Game"""
import random
import sys


class RPS:
    """Game class"""

    def __init__(self):
        print("Welcome to RPS 9000!")
        self.user_score: int = 0
        self.ai_score: int = 0

        self.moves: dict = {
            'rock': '(rock)', 'paper': '(paper)', 'scissors': '(scissors)'}

        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        """Main game function"""
        user_move: str = input('Rock, paper, scissors? >> ').lower()

        if user_move == 'exit':
            print('Thanks for playing RPS 9000!')
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move ...")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        """display user and ai moves"""
        print('______________________')
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")
        print('______________________')

    def check_moves(self, user_move: str, ai_move: str):
        '''Determine the winner'''
        if user_move == ai_move:
            print('It\'s a tie!')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
            self.user_score += 1
            print(f"User: {self.user_score} | AI: {self.ai_score}")
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
            self.user_score += 1
            print(f"User: {self.user_score} | AI: {self.ai_score}")
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
            self.user_score += 1
            print(f"User: {self.user_score} | AI: {self.ai_score}")
        else:
            print('AI wins!')
            self.ai_score += 1
            print(f"User: {self.user_score} | AI: {self.ai_score}")


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
