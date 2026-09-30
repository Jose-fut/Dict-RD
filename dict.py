palabras_dominicanas = {
    "Grajo": "Es para decir que alguien tiene mal olor",
    "tiguere": "Alguien que es muy vivo y travieso",
    "vaina": "Es una forma para referirse a algo no definido"
}

palabra = input("Escribe una palabra que no entiendas: ")

if palabra in palabras_dominicanas:
    print("SIGNIFICADO:", palabras_dominicanas[palabra])
else:
    print("NO SE HA ENCONTRADO LO QUE BUSCA")
