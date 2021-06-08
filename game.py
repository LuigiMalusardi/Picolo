import random
from player import Player
from phrases import *
from settings import Settings

class Game:

    def __init__(self):
        self.action_incr_num = 0
        self.settings = Settings()
        self.action_types = ['giochi','obblighi','shots','virus']
        self.type_weights = [40,40,5,15]
        self.action_type = ''
        self.action_text = ''
        self.players = []
        self.active_virus = []
        self.prob_virus = 0.5

        json_data = load_data('phrases.json')
        #Prelevo le frasi GIOCHI, le mescolo e creo indice a 0
        self.giochi_list = load_giochi(json_data)
        random.shuffle(self.giochi_list)
        self.giochi_index = 0

        #Prelevo le frasi OBBLIGHI, le mescolo e creo indice a 0
        self.obblighi_list = load_obblighi(json_data)
        random.shuffle(self.obblighi_list)
        self.obblighi_index = 0

        #Prelevo le frasi SHOTTINI, le mescolo e creo indice a 0
        self.shots_list = load_shots(json_data)
        random.shuffle(self.shots_list)
        self.shots_index = 0

        #Prelevo le frasi VIRUS, le mescolo e creo indice a 0
        self.virus_list = load_virus(json_data)
        random.shuffle(self.virus_list)
        self.virus_index = 0

    def is_enough_players(self):
        #Controlla se ci sono abbastanza giocatori
        if len(self.players) < self.settings.min_players:
            return False
        
        return True

    def next_action_task(self):
        #Sceglie il tipo e la frase da mostrare
        #Gioco terminato
        if self.action_incr_num >= self.settings.action_max_number:
            self.action_type = 'FINE'
            self.action_text = 'Gioco terminato!'
            return

        #Tipo di azione random
        self.action_type = random.choices(self.action_types,weights=self.type_weights,k=1)[0]

        #Modifica la percentuale virus in base all'attuale stato gioco
        self.mod_perc_virus()

        #Se devo rimuovere un virus
        if self.prob_virus == 1:
            self.action_type = 'virus'

        if self.action_type == 'giochi':
            self.action_text = self.giochi_list[self.giochi_index]
            self.giochi_index += 1

        elif self.action_type == 'obblighi':
            self.action_text = self.obblighi_list[self.obblighi_index]
            self.obblighi_index += 1

        elif self.action_type == 'shots':
            self.action_text = self.shots_list[self.shots_index]
            self.shots_index += 1

        elif self.action_type == 'virus':
            #Se non ci sono virus attivi entro per forza nell'IF
            if random.random() >= self.prob_virus or len(self.active_virus) <= 0:
                #50% di probabilità di attivare un nuovo virus
                virus = self.virus_list[self.virus_index]
                self.virus_index += 1

                #Cerco un player non infetto
                vittima = random.choice([p for p in self.players if not p.infected])
                helpers = random.sample([p for p in self.players if p != vittima],k=2)

                #Attivo virus
                self.active_virus.append(virus)
                self.action_text = virus.activate(vittima,helpers)
            else:
                #50% di probabilità di disattivare un nuovo virus
                virus = random.choice(self.active_virus)
                self.action_text = virus.deactivate()
                self.active_virus.remove(virus)
            
            #Incremento numero azioni
            self.action_incr_num += 1
            return

        #Sostituisco con i nomi e incremento numero azioni
        self.action_text = self.action_set_names(self.action_text)
        self.action_incr_num += 1
        
    def get_next_action_data(self):
        #Restituisco tuple con dati azione
        return self.action_type,self.action_text

    def action_set_names(self,action_txt):
        #Imposta i nomi in modo random
        n_player_req = action_txt.count('$')
        players = random.sample(self.players,k=n_player_req)
        for n in range(n_player_req):
            action_txt = action_txt.replace(f'${n+1}',players[n].name)
        
        return action_txt

    def mod_perc_virus(self):
        #Modifica la percentuale di uscita del virus
        #>= VAL -> nuovo virus
        # < VAL -> vecchio virus

        remaining_actions = self.settings.action_max_number - self.action_incr_num

        if remaining_actions <= len(self.active_virus) or len(self.active_virus) >= 3:
            self.prob_virus = 1 #Rimuovo sicuramente un virus
        
    def add_player(self,p_name):
        #Aggiunge il giocatore alla partita
        self.players.append(Player(p_name))

    def remove_player(self,p_name):
        #Rimuove dalla partita il giocatore con il nome selezionato
        for p in self.players:
            if p.name == p_name:
                self.players.remove(p)
                break
        return False

    def remove_player(self,player):
        #Rimuove dalla partita il giocatore selezionato
        if player not in self.players:
            return False

        self.players.remove(player)

    def reset(self):
        self.action_incr_num = 0
        self.settings = Settings()
        self.action_types = ['giochi','obblighi','shots','virus']
        self.type_weights = [40,40,5,15]
        self.action_type = ''
        self.action_text = ''
        self.players = []
        self.active_virus = []
        self.prob_virus = 0.5

        random.shuffle(self.giochi_list)
        self.giochi_index = 0

        random.shuffle(self.obblighi_list)
        self.obblighi_index = 0

        random.shuffle(self.shots_list)
        self.shots_index = 0

        random.shuffle(self.virus_list)
        self.virus_index = 0
    