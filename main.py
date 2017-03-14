from random import randrange

player1roll1=randrange(1,4)
player1roll2=randrange(1,6)
player1roll3=randrange(1,12)
player1roll4=randrange(1,20)
player2roll1=randrange(1,4)
player2roll2=randrange(1,6)
player2roll3=randrange(1,12)
player2roll4=randrange(1,20)

wincount=3
player1score=player1roll1 + player1roll2 + player1roll3 + player1roll4
player2score=player2roll1 + player2roll2 + player2roll3 + player2roll4 



while(player1score != 3 and player2score != 3):
    player1roll1 = randrange(1,4)
    player1roll2 = randrange(1,6)
    player1roll3 = randrange(1,12)
    player1roll4 = randrange(1,20)
    player2roll1 = randrange(1,4)
    player2roll2 = randrange(1,6)
    player2roll3 = randrange(1,12)
    player2roll4 = randrange(1,20)
    
    if(player1roll > player2roll):
	    print("player1score")
            player1score = player1score + 1
            print(player1score)
    if(player2roll > player1roll):
	    print("player2score")
            player2score = player2score + 1
            print(player2score)
    if(player1roll == player2roll):
        print("tie")
    if(player1score == 3):
    	print("PLAYER 1 WINS!")
    if(player2score == 3):
    	print("PLAYER 2 WINS!")
