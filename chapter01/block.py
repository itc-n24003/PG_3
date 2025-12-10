name="Mary"
#password="swordfish" #あえてコメントアウト
print("パスワードを入力してください")
password=input()
if name == "Mary":
    print("Hello, Mary!")
    if password == "swordfish":
        print("認証しました")
    else:
        print("パスワードが間違ってます")
else:
    print("名前が間違っています")