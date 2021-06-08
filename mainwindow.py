import tkinter as tk

class MainWindow(tk.Frame):

    def __init__(self, master=None,game=None):
        super().__init__(master)
        self.master = master
        self.game = game
        self.grid(row=0,column=0,sticky=tk.NSEW)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(3,weight=1)

        #Title label
        self.type_title = tk.StringVar(self)
        self.title_lbl = tk.Label(self,textvariable=self.type_title,font=("Arial", 16, "bold"))

        #Action label
        self.action_txt = tk.StringVar(self)
        self.action_lbl = tk.Label(self,textvariable=self.action_txt,font=("Arial", 12),height=3,wraplength=580)

        #Continue button
        self.continue_btn = tk.Button(self,text='Avanti',command=self.on_continue_press,font=('Arial',20))

        #Exit button
        self.exit_btn = tk.Button(self,text='Exit',command=self.on_exit_press)

        #Virus listbox
        virus_reminder = ''
        #Per ogni virus attivo inserisco il testo come reminder
        for v in self.game.active_virus:
            virus_reminder += '- ' + v.active_complete_txt + '\n'
        self.virus_txt = tk.StringVar(self)
        self.virus_txt_message = tk.Label(self,textvariable=self.virus_txt,anchor=tk.W,height=5)
        self.virus_txt.set(virus_reminder)

        #Grid layout
        self.title_lbl.grid(row=0,column=0,columnspan=2)
        self.action_lbl.grid(row=1,column=0,columnspan=2,sticky=tk.NSEW,pady=30)
        self.continue_btn.grid(row=2,column=0,columnspan=2,pady=20)
        self.exit_btn.grid(row=3,column=0,ipadx=5)
        self.virus_txt_message.grid(row=3,column=1,sticky=tk.NSEW)

    def on_exit_press(self):
        #Azione alla pressione del pulsante exit
        #Torno alla start window
        self.master.showStart()
        self.continue_btn.config(text='Continua',command=self.on_continue_press)
        self.game.reset()

    def on_continue_press(self,event=None):
        #Chiamo nuova azione e salvo parametri type, text e attivazione virus
        self.game.next_action_task()
        a_type,a_txt = self.game.get_next_action_data()

        #Titolo in maiuscolo
        a_type = a_type.upper()
        #Imposto a schermo i vari testi
        self.action_txt.set(a_txt)
        self.type_title.set(a_type)
        virus_reminder = ''
        for v in self.game.active_virus:
            virus_reminder += '- ' + v.active_complete_txt + '\n'
        self.virus_txt.set(virus_reminder)

        #Se gioco finito converto btn continua in btn esci
        if self.game.action_type == 'FINE':
            self.continue_btn.config(text='Esci',command=self.on_exit_press)


