N = int(input())
card_list=[[0 for i in range(14)] for j in range(4)]
exist_card=[]

type_list = {0:"S",1:"H",2:"C",3:"D"}

for i in range(N):
    card = input().split()
    exist_card.append([card[0],int(card[1])])





for card in exist_card:
    card_num = int(card[1])
    if card[0] == "S":
        card_list[0][card_num] = 1
    elif card[0] == "H":
        card_list[1][card_num] = 1
    elif card[0] == "C":
        card_list[2][card_num] = 1
    elif card[0] == "D":
        card_list[3][card_num] = 1

#print(card_list)

for card_type in range(4):
    for i in range(1,14):
        if card_list[card_type][i] == 0:
            print("{} {}".format(type_list[card_type],i))