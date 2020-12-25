import random
name=input("Your name please: ")
print("Best of Luck ", name)
d={"hockey":"India", "football":"France", "volleyball":"Nepal","baseball":"USA","cricket":"England", "taekwondo":"South Korea", "bandy":"Russia","tabletennis":"China", "rugby":"New Zealand", "wrestling":"Japan", "handball":"Iceland"}
games=["hockey", "football", 'kabbadi', 'volleyball', 'baseball', 'cricket', 'taekwondo', 'bandy', 'tabletennis', 'rugby', 'wrestling', 'handball']
#games=d.keys()
game=random.choice(games)
print("Guess the characters:")
chance=''
turns=14
while turns>0:
    f=0
    for i in game:
        #country=d[i]
        if i in chance:
            print(i)
        else:
            print("_")
            f+=1
    if f==0:
        print('Congrats!! You have won')
        print('The game is ',game, ", the national sport of", d[game] )
        break
    a=input("Guess the character:")
    chance+=a
    if a not in game:
        turns-=1
        print("Wrong")
        print("You have ", turns, " more chances")
        if turns==0:
