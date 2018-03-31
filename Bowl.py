test1='x x x x x x x x x x x x'
test2='9- 9- 9- 9- 9- 9- 9- 9- 9- 9-'
test3='5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5'
test4='1- 2/ 1- 1/ x 23 x 23 1/ x x x'




def frames1_9(throw_list, score):
    for i in range(0,9):
        if throw_list[i]=='x':
            score.append(10)
            try:
                if throw_list[i-1]=='x'and i>0:
                    score[i-1]+=10
                    try:    
                        if throw_list[i-2]=='x'and i>1:
                            score[i-2]+=10
                    except IndexError:
                        pass
            except IndexError:
                pass
            try:
                if throw_list[i-1][1]=='/'and i>0:
                    score[i-1]+=10
            except IndexError:
                pass
        else:
            if throw_list[i][0]=='-':
                score.append(0)
            else:
                score.append(int(throw_list[i][0]))
                try:
                    if throw_list[i-1]=='x'and i>0:
                        score[i-1]+=(int(throw_list[i][0]))
                except IndexError:
                    pass
                try:    
                    if throw_list[i-2]=='x'and i>1 and throw_list[i-1]=='x':
                        score[i-2]+=(int(throw_list[i][0]))
                except IndexError:
                    pass
                try:
                    if throw_list[i-1][1]=='/'and i>0:
                        score[i-1]+=(int(throw_list[i][0]))
                except IndexError:
                    pass
            if throw_list[i][1]=='-':
                score[i]+=0
            elif throw_list[i][1]=='/':
                try:
                    if throw_list[i-1]=='x'and i>0:
                        score[i-1]+=(10-score[i])
                except IndexError:
                    pass
                score[i]=10
            else:
                score[i]+=int(throw_list[i][1])
                try:
                    if throw_list[i-1]=='x'and i>0:
                            score[i-1]+=int(throw_list[i][1])
                except IndexError:
                    pass

                else:
                    pass   
    return score



def frame10(throw_list, score):
    if throw_list[9][0]=='x':
        score.append(10)
        if throw_list[8]=='x':
            score[8]+=10
            if throw_list[7]=='x':
                score[7]+=10
        try:
            if throw_list[8][1]=='/':
                        score[8]+=10
        except IndexError:
            pass
        if throw_list[10][0]=='x':
            score[9]+=10
            if throw_list[8]=='x':
                score[8]+=10
            if throw_list[11][0]=='x': 
                score[9]+=10
            elif throw_list[11][0]=='-':
                pass
            else:
                score[9]+=(int(throw_list[11]))
        elif throw_list[10][0]=='-':
            if throw_list[11][0]=='x': 
                score[9]+=20
            elif throw_list[11][0]=='-':
                pass
            else:
                score[9]+=(int(throw_list[11]))
        else:
            score[9]+= (int(throw_list[10][0]))
            if throw_list[10][1]=='/':
                score[9]+=10-(int(throw_list[10][0]))
            elif throw_list[10][1]=='-':
                pass
            else:
                score[9]+= (int(throw_list[10][1]))


            if throw_list[8]=='x':
                score[8]+= (int(throw_list[11]))
    else:
        if throw_list[9][0]=='-':
            score.append(0)
        else:
            score.append(int(throw_list[9][0]))
            if throw_list[8][0]=='x':
                    score[8]+=(int(throw_list[9][0]))
            try:
                if throw_list[8][1]=='/':
                    score[8]+=(int(throw_list[9][0]))
            except IndexError:
                pass
        if throw_list[9][1]=='/':
            score[9]=10
            if throw_list[8][0]=='x':
                    score[8]+=10-(int(throw_list[9][0]))
            if throw_list[9][2]=='-':
                pass
            elif throw_list[9][2]=='x':
                score[9]+=10
            else:
                score[9]+=(int(throw_list[9][2]))
    return score


def bowl_counter(test):
    throw_list=test.split()
    score=[]
    frames1_9(throw_list, score)
    frame10(throw_list, score)
    return score
    


print (bowl_counter(test1))
print (sum(bowl_counter(test1)))

print (bowl_counter(test2))
print (sum(bowl_counter(test2)))

print (bowl_counter(test3))
print (sum(bowl_counter(test3)))

print (bowl_counter(test4))
print (sum(bowl_counter(test4)))