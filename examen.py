def mediana(dic):
    keys=list(dic.keys())
    items=list(dic.items())
    lista=[]
    if len(items) % 2 !=0:
        for i in range(len(items)):
            lista.append(items[i][1])
        lista.sort()
        calculo=(len(items)/2)
        res=lista[int(calculo)]
        return(res)
    if len(items) % 2==0:
        for i in range(len(items)):
            lista.append(items[i][1])
        lista.sort()
        print(lista)
        calculo=(len(items)/2)
        media=(lista[int(calculo)]+lista[int(calculo-1)])/2
        print(lista[int(calculo)])



if __name__ == '__main__':
    diccionario={"valor0":5,"valor1":3,"valor2":8,"valor3":1,"valor4":6,"valor5":7,"valor6":10,"valor7":11}
    mediana(diccionario)
