from classes.game import Game

 
def main():
    while True:
        game = Game([],[])
        game.run_game()
        if game.show_exit_menu() == "2":
            print("goodby!")
            break

if __name__ == "__main__":
    main()