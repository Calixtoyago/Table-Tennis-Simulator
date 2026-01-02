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

# backspin, topspin, forehand, backhand, serve, attack, defense, double (duas maos)