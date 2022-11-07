dic = {
    "Alemania" : "Berlin",
    "Mexico" : "Ciudad de Mexico",
    "Francia" : "Paris"

}

print(dic["Alemania"])
dic["Argentina"]="Buenos aires"
print(dic)
del dic["Francia"]
print(dic)

tupla =("Mexico","USA" , "Alemania") #Creamos una tupla y dependiendo la posicion asignamos la clave

dic2 = {
    tupla[0]:"Ciudad de mexico",
    tupla[1]:"Wasington",
    tupla[2]:"Berlin"
}
print(dic2)
print(dic2["Mexico"])
print(dic.keys())
print(dic.values())
print(len(dic))