def check_card(card):
    if card == 10:
        return 0
    else:
        return card


first_pl = [int(card_num) for card_num in input().strip().split()]
sec_pl = [int(card_num) for card_num in input().strip().split()]

for turn in range(1, 1_000_001):

    first_pl_card = first_pl.pop(0)
    sec_pl_card = sec_pl.pop(0)

    if first_pl_card == 0 and sec_pl_card == 9:
        first_pl_card = 10
    if sec_pl_card == 0 and first_pl_card == 9:
        sec_pl_card = 10

    if first_pl_card > sec_pl_card:
        first_pl.append(check_card(first_pl_card))
        first_pl.append(check_card(sec_pl_card))
    else:
        sec_pl.append(check_card(first_pl_card))
        sec_pl.append(check_card(sec_pl_card))

    if not first_pl:
        print(f"second {turn}")
        break
    if not sec_pl:
        print(f"first {turn}")
        break
 
    if turn == 1_000_000:
        print("botva")