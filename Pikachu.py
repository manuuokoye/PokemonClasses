
class Pikachu:
    def __init__(self):
        self.name = "Pikachu"
        self.hp = 35
        self.pp = 350
    def max_stats(self):
        self.max_hp = 35
        self.max_pp = 350
    def bolt(self):
        self.pp -= 25
        self.damage = 27.5
    def tailwhip(self):
        self.pp -= 15
        self.damage = 10
    def lightning_strike(self):
        self.pp -= 50
        self.damage = 45
    def being_attacked(self, damage):
        self.hp -= damage
    def pokemon_center(self):
        self.max_stats()
        self.hp = self.max_hp
        self.pp = self.max_pp

    def check_poki(self):
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} needs to go to the hospital")
            self.pokemon_center()
            print(f"{self.name} has now been restored to full stats")
            print(self.hp,self.pp)

    def __str__(self):
        return f"{self.name} | HP: {self.hp}/35 | PP: {self.pp}/350"

p = Pikachu()
p.being_attacked(50)
p.check_poki()
print(p)
