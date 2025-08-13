import random as rd

def rol():
    min_vamue=1
    max_value=6
    rol=rd.randint(min_vamue,max_value)

    return rol

while True:
    player=input('enter the number of player(2 -4)')
    if player.isdigit():
        player=int(player)
        if 2<=player<=4:
            break
        else:
            print('Must be between 2-4 players')
    else:
        print('invalid try again')
max_sore=50
player_scores=[0 for _ in range(player)]

while max(player_scores)<max_sore:
    for player_inx in range(player):
        print('\n playar number',player_inx+1,'turn has started')
        print('your total score is ',player_scores[player_inx] ,'\n')
        current_score=0
        while True:
            shold_rol=input("would you like to roll('y')? ")
            if shold_rol.lower()!='y':
                break
            value= rol
            if value==1:
                print('you rolled a 1! turn done')
                current_score=0
                break
            else:
                current_score += value
                print('yousc rolled a:',value)

            print('ypur score is',current_score)
        player_scores[player_inx] +=current_score
        print('your total score is :',player_scores[player_inx])

max_sore=max(player_scores)
winning_idx=player_scores.index(max_sore)
print('player number',winning_idx +1,'is the winner with a score of :',max_sore
)