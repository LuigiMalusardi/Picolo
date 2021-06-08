import tkinter as tk
import tkinter.simpledialog

class StartWindow(tk.Frame):

    def __init__(self, master=None,game=None):
        super().__init__(master)
        self.master = master
        self.game = game
        self.grid(row=0,column=0,sticky=tk.NSEW)
        self.columnconfigure(5,weight=1)
        self.rowconfigure(4,weight=1)

        #Title label
        title_lbl = tk.Label(self,text='PICOLO GAME',font=("Arial", 16, "bold"))

        #Impostazioni
        self.menu = tk.Menu(self)
        self.setting_menu = tk.Menu(self.menu, tearoff=0)
        def impostazioni():
            self.game.settings.action_max_number = tk.simpledialog.askinteger('Impostazioni','Inserisci il numero di azioni da eseguire: ',
                                                                               initialvalue=self.game.settings.action_max_number)
        self.setting_menu.add_command(label="Impostazioni", command=impostazioni)
        def informazioni():
            tk.simpledialog.messagebox.showinfo('Informazioni','Picolo Game\nMade by Luigi Malusardi\nV.1.0')
        self.setting_menu.add_command(label="Info",command=informazioni)
        self.master.config(menu=self.setting_menu)

        ############################################################
        #Player entry Label
        self.player_entry_lbl = tk.Label(self,text='Inserisci un nuovo giocatore:')

        #Player entry field
        self.player_entry_field = tk.Entry(self)
        self.player_num = 0
        player_name_txt = tk.StringVar()
        player_name_txt.set(f'Giocatore{self.player_num+1}')
        self.player_entry_field['textvariable'] = player_name_txt
        
        
        #Player ListBox
        self.player_listbox = tk.Listbox(self)

        #Player entry btn
        def save_player(event=None):
            player_name = self.player_entry_field.get()
            player_name = player_name.capitalize()
            if player_name in self.player_listbox.get(0,tk.END):
                tk.simpledialog.messagebox.showwarning('Attenzione!','Giocatore già presente in partita!')
                return
            self.player_num += 1
            player_name_txt.set(f'Giocatore{self.player_num+1}')
            self.player_entry_field.select_range(0,tk.END)
            self.player_listbox.insert(0,player_name)

        self.player_entry_field.bind('<Key-Return>',save_player)
        self.player_entry_btn = tk.Button(self,command=save_player,text='Aggiungi')

        #Player delete btn
        def delete_player(event=None):
            selection =self.player_listbox.curselection()
            if len(selection) != 0:
                ind = selection[0]
                self.player_listbox.delete(ind)

        self.player_listbox.bind('<Key-Delete>',delete_player)
        self.player_delete_btn = tk.Button(self,command=delete_player,text='Elimina')

        #####################################################
    
        #Reset
        def reset():
            self.game.reset()
            self.player_listbox.delete(0,tk.END)

        self.reset_btn = tk.Button(self,command=reset,text='Reset')

        #Start game
        def start_game():
            #Aggiungo i giocatori
            for p in self.player_listbox.get(0,tk.END):
                self.game.add_player(p)

            #Controllo se sono abbastanza
            if not self.game.is_enough_players():
                tk.simpledialog.messagebox.showerror('Giocatori insufficienti','Il minimo numero di giocatori è 3')
                self.game.reset()
            else:
                self.master.showMain()
            
        self.start_game_btn = tk.Button(self,command=start_game,text='Start!')

        #Grid setup
        title_lbl.grid(row=0,column=0,columnspan=6)

        self.player_entry_lbl.grid(row=1,column=0,columnspan=2,padx=10)
        self.player_entry_field.grid(row=1,column=2,columnspan=2)
        self.player_entry_btn.grid(row=1,column=4,pady=5,padx=5)

        self.player_listbox.grid(row=2,column=0,columnspan=6,sticky=tk.EW,padx=5)

        self.player_delete_btn.grid(row=3,column=0,sticky=tk.W,padx=5)
        self.reset_btn.grid(row=3,column=4,padx=5,pady=5,sticky=tk.EW)
        self.start_game_btn.grid(row=3,column=5,padx=5,sticky=tk.EW)
        
       
        

        
        