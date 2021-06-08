import json
from virus import Virus

def load_data(json_path):
    #Carica i dati json
    data = json.load(open(json_path,encoding='utf-8'))
    return data

def load_giochi(data):
    #Restituisce le frasi GIOCHI
    return [g for g in data['giochi']]

def load_obblighi(data):
    #Restituisce le frasi OBBLIGHI
    return [o for o in data['obblighi']]

def load_shots(data):
    #Restituisce le frasi SHOTTINI
    return [s for s in data['shots']]

def load_virus(data):
    #Restituisce le frasi VIRUS
    virus_on = [v_on for v_on in data['virus_on']]
    virus_off = [v_off for v_off in data['virus_off']]

    #Se le lunghezze non corrispondono return FALSE
    if len(virus_on) != len(virus_off):
        return False
    else:
        #Restituisco una lista di oggetti Virus
        virus_phrases = list(zip(virus_on,virus_off))
        virus_lst = []
        for v in virus_phrases:
            virus_lst.append(Virus(v[0],v[1]))

        return virus_lst