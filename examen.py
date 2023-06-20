import csv
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
      
        calculo=(len(items)/2)
        media=(lista[int(calculo)]+lista[int(calculo-1)])/2
        
        return media

def procesar(nombre,curso):
    lista=[]
    listafiltrada=[]
    cont=0
    with open(nombre + '.csv', 'r') as file:
            reader = csv.reader(file)
            
            primera_fila = next(reader)  # Lee la primera fila
            for fila in reader:
                lista.append(fila)
            for casilla in lista:
                
                if int(casilla[len(casilla)-1]) == curso:
                    
                    listafiltrada.append(casilla)
                    cont=cont+1
                
                    
    if cont!=0:
        return listafiltrada
    else:
        raise ValueError("No hay ningún alumno en el curso: "+str(curso))
                       
                
                
    
        

if __name__ == '__main__':
    diccionario={"valor0":5,"valor1":3,"valor2":8,"valor3":1,"valor4":6,"valor5":7,"valor6":10,"valor7":11}
    res=mediana(diccionario)
    print("valor mediana a devolver:"+str(res))

    listafiltrada=procesar("fichero",3)
    print("La lista de alumnos es: "+str(listafiltrada))
