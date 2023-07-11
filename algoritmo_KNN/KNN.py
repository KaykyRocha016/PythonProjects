def euclidian(a,b,c,d):
  distancia=((a**2)+(b**2)+(c**2)+(d**2))**(1/2)
  
  return distancia
  

def read_and_list():
  matriz=[]

  arq=open('iris.data.csv','r')
  
  for linha in arq:
    info=linha.strip('\n')
    lista=info.split(',')
    matriz.append(lista)
  
  return matriz


def ordem_crescente():
  dados_brutos=read_and_list()
  classificados=[]
  
  i=1
  while i in range(len(dados_brutos)):
    classificação=[]
    elemento=euclidian(float(dados_brutos[i][0]),float(dados_brutos[i][1]),float(dados_brutos[i][2]),float(dados_brutos[i][3]))
    classificação.append(elemento)
    classificação.append(dados_brutos[i][4])
    classificados.append(classificação)

    i+=1
  classificados.sort(key=lambda x:x[0])


  return classificados


def ler_arquivo():
  dados=[]
  arquivo_lido=input('qual o nome do arquivo?: ')
  dados_novos=arquivo_lido
  arq=open(dados_novos,'r')
  
  for elem in arq:
    info=elem.strip('\n')
    lista=info.split(',')
    dados.append(lista)
  arquivo_lido=''
  
  return dados



def dados_arq_novo():
  dados_euclidianos_novos=[]
  dados=ler_arquivo()
  
  for i in range(len(dados)):
    converter=euclidian(float(dados[i][1]), float(dados[i][2]),float(dados[i][0]), float(dados[i][3]))
    dados_euclidianos_novos.append(converter)
 

  
  return dados_euclidianos_novos


def comparar(k):
  j=0
  l=0
  setosa=0
  versicolor=0
  virginica=0
  i=0
  espécies=[]
  
    
  for elem in dados_arq_novo():
    i=0
    l=0
    while i<len(ordem_crescente()) and elem>ordem_crescente()[i][0]:
      i+=1


    
    m=i-1 
    while l<k:
      if ordem_crescente()[m][1]=='versicolor':
        versicolor+=1
        m-=1
        l+=1

      if ordem_crescente()[i][1]=='versicolor':
        versicolor+=1
        i+=1
        l+=1

      if ordem_crescente()[m][1]=='virginica':
        virginica+=1
      m-=1
      l+=1    

      if ordem_crescente()[i][1]=='virginica':
        virginica+=1
        i+=1
    
        l+=1

      if ordem_crescente()[m][1]=='setosa':
        setosa+=1
        m-=1
        l+=1  

      if ordem_crescente()[i][1]=='setosa':
        setosa+=1
        i+=1
        l+=1   

  
    if setosa>virginica>versicolor:

      espécies.append('setosa')

    elif setosa>versicolor>virginica:
 
      espécies.append('setosa')
    elif virginica>setosa>versicolor:

      espécies.append('virginica')
    elif virginica>versicolor>setosa:
 
      espécies.append('virginica')
    else:

        espécies.append('versicolor')
     
  
  return espécies




def main():
  k=int(input('qual K deseja utilizar?:'))
  especies=comparar(k)
  for elem in especies:
    print(elem)

main()




    


















        


