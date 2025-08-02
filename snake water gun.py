import random as r

selector = ["Snake", "Water", "Gun"]
player_choice = input("Snake, Water, or Gun?: ")

r_matrix = [
    ["Draw", "Win", "Lose"],
    ["Lose", "Draw", "Win"],
    ["Win", "Lose", "Draw"]
]

if player_choice not in selector:
    print("Invalid Choice")
else:
    machine_choice = r.choice(selector)
    print("Machine Selected: ", machine_choice)

    p_index = selector.index(player_choice)
    m_index = selector.index(machine_choice)

    result = r_matrix[p_index][m_index]
    print("Player", result, "This Round")
