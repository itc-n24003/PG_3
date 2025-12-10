import random

while True:
    print("ここは後回し")
    break


computer_move = random.randint(0,2)

if computer_move == player_move:
    print("あいこです")
    ties += 1
else:
    if computer_move == "0":
        print("コンピューター:グー ", end="")
        if player_move == "1":
            print("あなた: チョキ ...あなたの負けです")
            loses += 1
        else:
            print("あなた: グー ...あなたの勝ちです")
            wins += 1
    elif computer_move == "1":
        print("コンピューター: チョキ ", end="")
        if player_move == "0":
            print("あなた: グー ...あたなたの勝ちです")
            wins += 1
        else:
            print("あなた: パー　...あなたの負けです")
            loses += 1
    else:
        print("コンピューター: パー ", end="")
        if player_move == "0":
            print("あなた: グー ...あなたの負けです")
            loses += 1
        else:
            print("あなた: チョキ ...あなたの勝ちです")
            wins += 1