score = []

def calc_score(your_move, opponent_move):
    global score

    # lose to paper (rock)

    if your_move == "X" and opponent_move == "B":
        score.append(1)

    # draw with scissors (scissors)

    if your_move == "Y" and opponent_move == "C":
        score.append(3)
        score.append(3)

    # win against rock (paper)

    if your_move == "Z" and opponent_move == "A":
        score.append(6)
        score.append(2)

    # lose to scissors (paper)

    if your_move == "X" and opponent_move == "C":
        score.append(2)

    # win vs paper (scissors)

    if your_move == "Z" and opponent_move == "B":
        score.append(6)
        score.append(3)

# draw vs rock

    if your_move == "Y" and opponent_move == "A":
        score.append(3)
        score.append(1)

    #lose against rock (scissors)

    if your_move == "X" and opponent_move == "A":
        score.append(3)

    #draw against paper
    if your_move == "Y" and opponent_move == "B":
        score.append(2)
        score.append(3)

    #win against scissors (rock)
    if your_move == "Z" and opponent_move == "C":
        score.append(6)
        score.append(1)

with open("input.txt") as file:
    for line in file:
        line.strip()
        moves = line.split(" ")
        calc_score(opponent_move = moves[0].strip(), your_move = moves[1].strip())



print(score)
final_score = sum(score)
print(final_score)



