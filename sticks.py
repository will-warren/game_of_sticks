from random import choice
#import system.io

class Player:

    def __init__(self, name, lose_bool=False):
        self.name = name
        self.lose_bool = lose_bool

    def __str__(self):
        return "Player name: {}".format(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def get_move(self, game, test_bool):
        move = 0
        if not test_bool:
            move = int(input("\nHow many sticks do you want to pick up, {}? (1-3)".format(self.name)))
            while move < 1 or move > 3:
                print("That wasn't a valid choice, {}".format(self.name))
                move = int(input("\nHow many sticks do you want to pick up, {}? (1-3)".format(self.name)))
            self.moves_list.append(move)
        return move

class Game:
    def __init__(self, stick_total, player1, player2="none"):
        self.player1 = player1
        self.player2 = player2
        self.stick_total = stick_total
        self.stick_num = stick_total

    def __str__(self):
        return "This game is between {} and {} with {} sticks.".format(self.player1, self.player2, self.stick_num)


    def __eq__(self, other):
        return (self.player1 == other.player1 and
               self.player2 == other.player2 and
               self.stick_num == other.stick_num)

class AI:

    def __init__(self, game):
        self.name = "AI"
        self.temp_moves_list = []
        self.lose_bool = False
        # self.all_poss_moves_dict = enumerate([[1,2,3]] * game.stick_num, 1)
        self.all_poss_moves_dict = {x+1: [1,2,3] for x in range(game.stick_num)}


    def __str__(self):
        return "AI"

    def __eq__(self, other):
        return (self.name == other.name and
        self.all_poss_moves_dict == other.all_poss_moves_dict)

    def get_move(self, game, test_bool):
        move = 0
        if not test_bool:
            if game.stick_num > len(self.all_poss_moves_dict):
                for x in range(len(self.all_poss_moves_dict), game.stick_num + 4):
                    self.all_poss_moves_dict[x]= [1,2,3]
            move = choice(self.all_poss_moves_dict[game.stick_num])
            self.temp_moves_list.append((game.stick_num,move))
            print("The computer picked up {} sticks.".format(move))
        return move

    def save_moves(self):
        for chunk in self.temp_moves_list:
            self.all_poss_moves_dict[chunk[0]].append(chunk[1])
            self.temp_moves_list = []


        """dumb AI strategy"""

        # if game.stick_num < 3:
        #     move = choice([1,2])
        #     self.temp_moves_list.append(move)
        #     print("The computer picked up {} sticks.".format(move))
        #     return move
        # else:
        #     move = 3
        #     self.temp_moves_list.append(move)
        #     print("The computer picked up {} sticks.".format(move))
        #     return move

def user_turn(name, game, test_bool):
    if not test_bool:
        print("\nSticks remaining: {}".format(game.stick_num))
        move = name.get_move(game, False)
        game.stick_num -= move
    if game.stick_num <= 0:
        name.lose_bool = True


def main():
    #system.io.clear()
    print("Welcome to the game of sticks!\n\n")
    while True:
        choice = int(input("How many players? (1 or 2) "))
        if choice == 1:
            player1_name = input("What is Player 1's name? ")
            break
        elif choice == 2:
            player1_name = input("What is Player 1's name? ")
            player2_name = input("What is Player 2's name? ")
            break
        else:
            print("That was not a correct choice. Try again")

    # input loop
    if choice == 2:
        while  True:
            stick_total = int(input("How many sticks are on the table initially (10-100)? "))
            if stick_total >= 10 and stick_total <= 100:
                break
        this_game = Game(stick_total, player1_name, player2_name)
        player1 = Player(player1_name)
        player2 = Player(player2_name)

        # game loop
        while this_game.stick_num > 0:
            user_turn(player1, this_game)
            if player1.lose_bool:
                break
            user_turn(player2, this_game)


        if player1.lose_bool:
            print("\n\nGame Over!  Congrats, {}, you win! Better luck next time, {}.\n".format(player2.name, player1.name))
        else:
            print("\n\nGame Over!  Congrats, {}, you win! Better luck next time, {}.\n".format(player1.name, player2.name))
    else:
        while  True:
            stick_total = int(input("How many sticks are on the table initially (10-100)? "))
            if stick_total >= 10 and stick_total <= 100:
                break
        this_game = Game(stick_total, player1_name)
        ai = AI(this_game)
        player1 = Player(player1_name)

        while(True):
            #game_loop
            # game loop
            while this_game.stick_num > 0:
                user_turn(player1, this_game)
                if this_game.stick_num == 0:
                    break
                user_turn(ai, this_game)

            if player1.lose_bool:
                print("\n\nGame Over!  The computer won! Better luck next time, {}.\n".format(player1.name))
                ai.save_moves()
                play_again = input("Do you want to play again? [Y/n] ")
                if play_again == 'Y':
                    player1.lose_bool = False
                    ai.lose_bool = False
                    while this_game.stick_num < 10 or this_game.stick_num > 100:
                        this_game.stick_num = int(input("How many sticks are on the table initially (10-100)? "))
                        if stick_total >= 10 and stick_total <= 100:
                            break
                else:
                    break
            else:
                print("\n\nGame Over!  Congrats, {}, you beat the computer!\n".format(player1.name))
                play_again = input("Do you want to play again? [Y/n] ")
                if play_again == 'Y':
                    player1.lose_bool = False
                    ai.lose_bool = False
                    while this_game.stick_num < 10 or this_game.stick_num > 100:
                        this_game.stick_num = int(input("How many sticks are on the table initially (10-100)? "))
                        if stick_total >= 10 and stick_total <= 100:
                            break
                else:
                    break

#main()
