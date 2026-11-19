from classes.card import Card
from classes.player import Player
import random

class Game:
    def __init__(self,deck:list[Card],players:list[Player]):
        
        self.deck = deck 
        self.players = players 

    def create_deck(self):
        types = ["H","D","S","C"]  
        for type in types:
            for i in range(13):
                self.deck.append(Card(type,i+2))

    def create_players(self):
        player = Player("player",[])
        computer = Player("computer",[])
        for side in [player,computer]:
            self.players.append(side)

    def shuffle_deck(self):
        count = 0
        while count <= 1000: 
            index_1 = random.randint(1,51)
            index_2 = random.randint(1,51)
            if index_1 != index_2:
                first_card = self.deck[index_1]
                self.deck[index_1] = self.deck[index_2]
                self.deck[index_2] = first_card
                count += 1

    def dealing_cards(self):
        for i in range(len(self.deck) // 2):
            for player in self.players:
                player.cards.append(self.deck.pop(0))

    def add_card(self,computer_card,player_card,type:str | None = None):
        player = self.players[0]
        computer = self.players[1]
        if type:
            if type.lower() == "player":
                player.cards.append(computer_card)
                player.cards.append(player_card)
            elif type.lower() == "computer":
                computer.cards.append(computer_card)
                computer.cards.append(player_card)
        else:
            player.cards.append(player_card)
            computer.cards.append(computer_card)

    # An edge case, where a player comes to 0 cards (almost impossible) 
    def check_zero_cards(self,cards,player):
        if cards == 0:
            print(f"\nThe game can not carry on!\n{player} with zero cards")
            return False
        return True

    def display_end_game(self,rounds,computer_num,player_num):
        print("===================== END GAME =========================")
        print(f"• rounds: {rounds}")
        if computer_num > player_num:
            massage = "Computer wins the game!" 
        elif player_num > computer_num:
            massage = "Player wins the game!"
        else:
            massage = "drow!"
        print(f"• Computer cards: {computer_num}")
        print(f"• Player cards: {player_num}")
        print(f"• {massage}") 
        print("========================================================")        


    def display_turn(self):
        print("\n• ========== TURN ==========")
        player = self.players[0]
        computer = self.players[1]
        player_card = player.draw_card()
        computer_card = computer.draw_card()
        print(f"• Player: {player.display_card(player_card.value)} {player_card.type}")
        print(f"• Computer: {computer.display_card(computer_card.value)} {computer_card.type}")
        if player_card.value > computer_card.value:
            self.add_card(computer_card,player_card,"player")
            print(f"• Player won the round!")
        elif computer_card.value > player_card.value:
            self.add_card(computer_card,player_card,"computer")
            print("• Computer won the round!")
        else:
            self.add_card(computer_card,player_card)
            print("• Its a draw!")
        print(f"• Player cards: {len(player.cards)} | Computer cards: {len(computer.cards)}")
        print("• ==========================")
        if not self.check_zero_cards(len(player.cards),"player") or not self.check_zero_cards(len(computer.cards),"computer"):
            return False


    def show_menu(self):
        valid = False
        while not valid:
            choise = input("""
• 1. Play turn
• 2. Exit

• Choose (1/2): """)
            if choise in ["1","2"]:
                return choise 
            print("\nNot valid choise\n")

    def show_exit_menu(self):
        valid = False
        while not valid:
            choise = input("""

• 1. New game
• 2. Exit

• Choose: """)
            if choise in ["1","2"]:
                return choise
            print("\nNot valid choise\n")

    def run_game(self):
        print("\n==========================")
        print("   WELCOME TO WAR GAME")
        print("==========================")
        self.create_deck()
        self.create_players()
        self.shuffle_deck()
        self.dealing_cards()
        rounds = 0
        while True:
            choise = self.show_menu()
            if choise == "2":
                self.display_end_game(rounds,len(self.players[1].cards),len(self.players[0].cards))
                break                        
            elif choise == "1":
                if self.display_turn() == False:
                    self.display_end_game(rounds,len(self.players[1].cards),len(self.players[0].cards))
                    break 
                rounds += 1
                
