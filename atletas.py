class Atleta:
    def __init__(self, nome, ataque, defesa, saque):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.saque = saque
    
    def __str__(self):
        return f'''
Atleta: {self.nome}
Ataque: {self.ataque}
Defesa: {self.defesa}'''


calderano = Atleta('Hugo Calderano', 18, 17, 7)
truls = Atleta('Truls Möregårdh', 16, 15, 8)
bruna_takahashi = Atleta('Bruna Takahashi', 14, 16, 7)
giulia_takahashi = Atleta('Giulia Takahashi', 13, 15, 16)
felix_lebrun = Atleta('Félix Lebrun', 19, 15, 9)
chuqin = Atleta('Wang Chuqin', 19, 18, 9)

atletas = [
    calderano, truls, 
    bruna_takahashi, giulia_takahashi,
    felix_lebrun, chuqin
]
# backspin, topspin, forehand, backhand, serve, ataque, defesa, double (duas maos)