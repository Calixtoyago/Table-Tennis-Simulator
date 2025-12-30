class Athlete:
    def __init__(self, name, attack, defense, serve):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.serve = serve
    
    def __str__(self):
        return f'''
Athlete: {self.name}
attack: {self.attack}
defense: {self.defense}
serve: {self.serve}'''


calderano = Athlete('Hugo Calderano', 18, 17, 7)
truls = Athlete('Truls Möregårdh', 16, 15, 8)
bruna_takahashi = Athlete('Bruna Takahashi', 14, 16, 7)
giulia_takahashi = Athlete('Giulia Takahashi', 13, 15, 16)
felix_lebrun = Athlete('Félix Lebrun', 19, 15, 9)
chuqin = Athlete('Wang Chuqin', 19, 18, 9)

athletes_list = [
    calderano, truls, 
    bruna_takahashi, giulia_takahashi,
    felix_lebrun, chuqin
]
# backspin, topspin, forehand, backhand, serve, attack, defense, double (duas maos)