from game import Game
import tkinter as tk
from startwindow import StartWindow
from mainwindow import MainWindow

class Controller(tk.Tk):

    def __init__(self,game):
        super().__init__()
        self.title("Picolo Game")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.minsize(600, 300)
        self.maxsize(600, 300)
        self.mMainWindow = MainWindow(self,game)
        self.mMainWindow.grid(row=0,column=0,sticky=tk.NSEW)
        self.mStartWindow = StartWindow(self,game)
        self.mStartWindow.grid(row=0,column=0,sticky=tk.NSEW)


    def showMain(self):
        #Mostra main window
        self.mMainWindow.tkraise()
        self.mMainWindow.on_continue_press()


    def showStart(self):
        #Mostra start window
        self.mStartWindow.tkraise()


if __name__ == '__main__':
    mGame = Game()
    mController = Controller(mGame)
    mController.mainloop()




def main():
    players_lst = ['Luigi','Sara','Cla','Fra','Ermes']
    game = Game()
    for p in players_lst:
        game.add_player(p)

    if not game.is_enough_players():
        print('Non ci sono abbastanza giocatori!')
    
    else:
        for i in range(5):
            action = game.next_action_task()
            action_type = game.action_type

            print(action_type)
            print(action,end='\n\n')