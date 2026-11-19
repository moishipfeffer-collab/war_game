from classes.card import Card

class Player:
    def __init__(self,name,cards:list[Card]):
        self.name = name 
        self.cards = cards

    def draw_card(self):
        card = self.cards.pop(0)
        return card

    def display_card(self,card_value):
        cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        return cards[card_value - 2]
        