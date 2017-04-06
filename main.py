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
player1score=0
player2score=0


while(player1score != 3 and player2score != 3):
    player1roll1 = randrange(1,4)
    player2roll1 = randrange(1,4)
    print(player2roll1,player1roll1)
    if(player1roll1 == 1 and player2roll1 == 1):
        print("TIE")
    if(player1roll1 == 1):
        print("PLAYER 1 WINS")
        player1score=3
    if(player1roll1 > player2roll1):
            print("player 1")
            player1score =+ 1
    if(player2roll1 > player1roll1):
            print("player 2")
            player2score =+ 1


    player1roll2 = randrange(1,6)
    player2roll2 = randrange(1,6)
    print(player1roll2,player2roll2)
    if(player1roll2 > player2roll2):
        print("player 1")
        player1score =+ 1
    if(player2roll2 > player2roll2):
        print("player 2")
        player2score =+ 1

    player1roll3 = randrange(1,12)
    player2roll3 = randrange(1,12)
    print(player1roll3,player2roll3)
    if(player1roll3 == 3):
        print("PLAYER 2 WINS")
    if(player1roll3 == 3 and player2roll3 == 3):
        print("TIE")
    if(player1roll3 > player2roll3):
        print("player 1")
        player1score =+ 1
    if(player2roll3 > player1roll3):
        print("player 2")
        player2score =+ 1

    player1roll4 = randrange(1,20)
    player2roll4 = randrange(1,20)
    print(player1roll4,player2roll4)
    if(player1roll4 > player2roll4):
        print("player 1")
        player1score =+ 1
    if(player2roll4 > player1roll4):
        print("player 2")
        player2score =+ 1
   
if(player1score == 3):
    print("PLAYER 1 WINS!")
if(player2score == 3):
    print("PLAYER 2 WINS!")
