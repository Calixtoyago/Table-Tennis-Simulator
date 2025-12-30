from math import floor

class Athlete:
    def __init__(self, name, attack, defense, serve):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.serve = serve
        self.overall = floor((attack + defense + serve) / 3)
    
    def __str__(self):
        return f'''
Athlete: {self.name}
OVR: {self.overall}
Attack: {self.attack}
Defense: {self.defense}
Serve: {self.serve}'''


bruna_takahashi = Athlete('Bruna Takahashi', 14, 16, 7)
felix_lebrun = Athlete('Félix Lebrun', 19, 15, 9)
giulia_takahashi = Athlete('Giulia Takahashi', 13, 15, 6)
hugo_calderano = Athlete('Hugo Calderano', 18, 17, 7)
truls_moregardh = Athlete('Truls Möregårdh', 16, 15, 8)
wanq_chuqin = Athlete('Wang Chuqin', 19, 18, 9)

athletes_list = [
    bruna_takahashi, felix_lebrun,
    giulia_takahashi, hugo_calderano,
    truls_moregardh, wanq_chuqin
]
# backspin, topspin, forehand, backhand, serve, attack, defense, double (duas maos)