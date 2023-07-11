qtd_alunos=int(input("quantos alunos farão a prova:"))
qtd_trabalhos=int(input("quantos trabalhos cada aluno fará:"))
i=0
#Kayky Bruno Rocha BES023, corrija com carinho
aprovados=0
recuperação=0
reprovados=0

soma_classe=0
numeração_alunos=0

while i<qtd_alunos:
    nota_p1=float(input("nota prova 1: "))
    nota_p2=float(input("nota prova 2: "))
    nota_sub=float(input("nota sub: "))
    
    if nota_sub>nota_p1:
        nota_p1=nota_sub
    
    elif nota_sub>nota_p2:
        nota_p2=nota_sub
    
    media_prova=(nota_p1 + nota_p2)/2
    i+=1
    j=0
    soma_trabalho=0
    numeração_trabalhos=1
    
    while j<qtd_trabalhos:
      nota_trabalho=float(input(f"nota no trabalho{numeração_trabalhos}:"))
      numeração_trabalhos+=1
      j+=1
    
      soma_trabalho+=nota_trabalho
    
    media_trabalho=soma_trabalho/(qtd_trabalhos)
    numeração_alunos+=1
    nota_aluno= (media_trabalho*0.4) + (media_prova*0.6)
    
    if nota_aluno>=6:
      print(f"nota do aluno{numeração_alunos}:", f"{nota_aluno:.2f}", "- aprovado")
      aprovados+=1
    
    elif nota_aluno>=4<6:
        print(f"nota do aluno {numeração_alunos}:"f"{nota_aluno:.2f}","- recuperação" )
        recuperação+=1
    
    else:
        print(f"nota do aluno {numeração_alunos}:",f"{nota_aluno:.2f}", "- reprovado")
        reprovados+=1    
    
    soma_classe+=nota_aluno
media_classe=soma_classe/qtd_alunos
print(f"media da classe: "f"{media_classe:.2f}")
print(f"aprovados: {aprovados}")
print(f"recuperação: {recuperação}")
print(f"reprovados: {reprovados}")

      

    
    
    
    


