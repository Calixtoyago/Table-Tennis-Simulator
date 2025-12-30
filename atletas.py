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


calderano = Atleta('Hugo Calderano', 15, 14, 7)
truls = Atleta('Truls Möregårdh', 14, 13, 7)

atletas = [calderano, truls]
# backspin, topspin, forehand, backhand, serve, ataque, defesa, double (duas maos)