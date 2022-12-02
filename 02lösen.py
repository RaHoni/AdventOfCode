score = 0
rock = "a"
paper = "b"
scissors = "c"
values = {"X":1,"Y":2,"Z":3,
          "A":1,"B":2,"C":3}


with open("02input") as file:
    for x in file.readlines():
        own:int = values.get(x[2])
        opponent = values.get(x[0])
        score+=own


        if opponent == own:
            score+=3
            #print("draw")
        elif opponent%3 == own-1:
            score+=6
            #print("win")
        else:
            #print("Loose")
            pass
        
print("First part" + str(score))

score = 0

with open("02input") as file:
    for x in file.readlines():
        own:int = values.get(x[2])
        opponent = values.get(x[0])



        if own == 1: # Lose
            tmp = (opponent+2) % 3
            if tmp == 0:
                tmp = 3
            score+= tmp
            #print(f"Lose {opponent}vs{tmp}")
        elif own == 2: # Draw
            score+=3 # Draw points
            score+= opponent # same as opponent
            #print(f"Draw ${opponent}vs${opponent}")
        else:
            score+= 6# Win
            score+= (opponent % 3) +1
            print(f"Win ${opponent}vs${(opponent % 3) +1}")
            pass

print(score)