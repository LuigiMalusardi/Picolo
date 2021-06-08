from player import Player

class Virus:

    def __init__(self,v_on = '',v_off = ''):
        self.victim = None
        self.helpers = []
        self.phrase_on = v_on
        self.phrase_off = v_off
        self.active = False
        self.seen = False

    def activate(self,vict = None,helpers = None):
        #Attiva virus e restituisce il testo ON con il nome vittima e gli helpers
        self.victim = vict
        self.victim.set_virus(self)
        self.helpers = helpers
        self.active = True

        virus_text = self.phrase_on.replace('$1', self.victim.name)

        if virus_text.find('$2') != -1:
            virus_text = virus_text.replace('$2',self.helpers[0].name)

        if virus_text.find('$3') != -1:
            virus_text = virus_text.replace('$3',self.helpers[1].name)

        self.active_complete_txt = virus_text
        return virus_text

    def deactivate(self):
        #Disattiva virus e restituisce il testo OFF con il nome vittima e gli helpers
        self.victim.remove_virus()
        virus_text = self.phrase_off.replace('$1', self.victim.name)

        if virus_text.find('$2') != -1:
            virus_text = virus_text.replace('$2',self.helpers[0].name)

        if virus_text.find('$3') != -1:
            virus_text = virus_text.replace('$3',self.helpers[1].name)
        
        self.victim = None
        self.helpers = None
        self.active = False
        self.seen = True

        return virus_text


        
