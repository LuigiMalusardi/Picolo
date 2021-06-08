
class Player:

    def __init__(self,name):
        self.name = name
        self.infected = False
        self.virus_active = None
    
    def set_virus(self,virus):
        #Infetta il soggetto con il virus ricevuto, tiene salvato un riferimento al virus con cui è colpito
        self.infected = True
        self.virus_active = virus
        return True

    def remove_virus(self):
        #Rimuove il virus dal soggetto
        self.infected = False
        self.virus_active = None
        
