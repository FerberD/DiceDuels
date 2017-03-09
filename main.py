from random import randrange

player1roll=randrange(1,6)
player2roll=randrange(1,6)

wincount=3
player1score=0
player2score=0


player1roll = randrange(1,6)
print(player1roll)
player2roll = randrange(1,6)
print(player2roll)

if(player1roll > player2roll):
	print("player1score")
player1score = player1score + 1
print(player1score)
if(player2roll > player1roll):
	print("player2score")
player2score = player2score + 1
print(player2score)
