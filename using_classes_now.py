import csv

with open('character.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


    class Characters:
        def __init__(self, name, element, hp, attack, defense):
            self.name = name
            self.element = element
            self.hp = hp
            self.attack = attack
            self.defense = defense

        def __str__(self):
            return (f"Name: {self.name}\n"
                    f"Element: {self.element}\n"
                    f"Hp: {self.hp}\n"
                    f"Attack: {self.attack}\n"
                    f"Defense: {self.defense}")


    hu_tao = Characters(name=input("Name: "), element=input("Element: "), hp=input("Hp: "),
                        attack=input("Attack: "), defense=input("Defense: "))

    ganyu = Characters(name=input("Name: "), element=input("Element: "), hp=input("Hp: "),
                       attack=input("Attack: "), defense=input("Defense: "))

    spamwriter.writerow([hu_tao])
    spamwriter.writerow([ganyu])
