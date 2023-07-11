pontos=list(map(int,input().split()))
placar=[]
frame=[]
pontuação_total=0
i=0
k=0
j=0
while k < len(pontos):
    if k==len(pontos)-3 and pontos[k]==10:#strike no ultimo frame
        pontuação_total+=pontos[k] + pontos[k+1] + pontos[k+2]
        break
    
    elif pontos[k]==10 and k+2<len(pontos):#strike antes do décimo frame
        pontuação_total+=pontos[k] + pontos[k+1] + pontos[k+2]
        k+=1
    
    elif pontos[k]+pontos[k+1]==10 and k+2<len(pontos):#spare
        pontuação_total+=10
        pontuação_total+=pontos[k+2]
        k+=2
    else:
        pontuação_total+=pontos[k]+pontos[k+1]
        k+=2

    
    


while i<len(pontos):
    j=0
    if i==len(pontos)-3 and pontos[i]==10:
        frame.append(pontos[i])
        frame.append(pontos[i+1])
        frame.append(pontos[i+2])
        placar.append(frame)
        frame=[]
        break
   
    
    elif pontos[i]==10:
        frame.append(pontos[i])
        placar.append(frame)
        frame=[]
        i+=1
   
    else:
        
        while j<=1 and i<len(pontos):
            frame.append(pontos[i])
            i+=1
            j+=1
        placar.append(frame)
        frame=[]

for elem in placar:
    if elem[0]==10:
        elem[0]='X _'
    
    print(elem, end="/ ")
print()


    
print(pontuação_total)







   