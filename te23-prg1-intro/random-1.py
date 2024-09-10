#bestäm om det är udde eller jämnt

#rulla tärningar

#vinnaren är det som bestämts

from random import randint

regler = input("Skriv om du vill spela Udda eller Jämnt: ")

computer = randint(1, 6)
player = randint(1, 6)
odd = (1,3,5)
even = (2,4,6)

if regler == "Udda" or regler == "udda":
    computer_result = computer in odd
    player_result = player in odd
    print("Datorn rullade {computer_result} och spelaren {player_result}, spel regeln var {regler}")
if computer_result == player_result:
    print("DU VANN! :D")
elif computer_result:
        print("HUHH!!!")
    else:
        print("WOW!")