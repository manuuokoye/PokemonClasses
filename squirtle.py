class Squirtle:
    def __init__(self):
        self.hp = 44
        self.pp = 300
        self.xp = 0
    def max_stats(self):
        self.max_hp = 44
        self.max_pp = 300
    def water_gun(self):
        self.pp -= 25
    def bite(self):
        self.pp -= 25
    def skull_bash(self):
        self.pp -= 10
    def hydro_pump(self):
        self.pp -= 5

    def being_attacked(self, damage):
        self.hp -= damage

    def pokemon_center(self):
        self.max_stats()
        self.hp = self.max_hp
        self.pp = self.max_pp

    def check_poki(self):
        if self.hp <= 0:
            self.hp = 0
            print("Squirtle needs to be taken to the hospital")
            self.pokemon_center()
            print("squirtle has been restored to max stats")
            print("hp:",self.hp,"pp:",self.pp)

s = Squirtle()
s.being_attacked(50)
s.check_poki()