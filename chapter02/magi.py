import random

#関数casper
def casper():
    kekka = random.randint(0, 1)
    if kekka == 0:
        print("casper ...可決")
    else:
        print("casper ...否決")
    return kekka
#関数blathasar
def blathasar():
    kekka = random.randint(0, 1)
    if kekka == 0:
        print("blathasar ...可決")
    else:
        print("blathasar ...否決")
    return kekka
#関数melchior
def melchior():
    kekka = random.randint(0, 1)
    if kekka == 0:
        print("melchior ...可決")
    else:
        print("melchior ...否決")
    return kekka
#プログラムここから
gidai=input("議題を入力してください >>")
print("審議中")

result=casper()+blathasar()+melchior()

print("[決議]")
if result > 1:
    print(f"議題「{gidai}」は否決されました")

else:
    print(f"議題「{gidai}」は可決されました")