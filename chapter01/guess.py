import random
secret_number = random.randint(1, 20)
print("1から20までの数を当てましょう")

for guesses_taken in range(1, 7):
    guess = int(input("数を入力してください->"))
    if guess < secret_number:
        print("あなたの推定値は小さいです")
    elif guess > secret_number:
        print("あなたの推定値は大きいです")
    else:
        break

if guess == secret_number:
    print(f"あたり！{guesses_taken}回で当たりました！")
else:
    print(f"残念正解は{secret_number}でした")