def building_a_character_hp():
    # Character's Hit Points
    try:
        character_hp = int(input("Enter character hp: "))
        if character_hp < 0:
            print("Enter a positive number.")
        else:
            print(f"HP: {character_hp}")
    except ValueError:
        print("Enter only integers.")


def building_a_character_atk():
    # Character attack
    try:
        character_attack = int(input("Enter character attack: "))
        if character_attack < 0:
            print("Enter a positive number.")
        else:
            print(f"Atk: {character_attack}")
    except ValueError:
        print("Enter only integers.")


def basic_info():
    name = input("Enter character name: ")
    element = input("Enter character element: ")
    print(f"Character: {name}")
    print(f"Element: {element}")


basic_info()
building_a_character_hp()
# building_a_character_atk()
