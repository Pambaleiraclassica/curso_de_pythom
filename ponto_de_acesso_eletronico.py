identidade=input("qual é o numero do seu BI?")
identidade.strip()
resultado = identidade.strip()
base_de_dados={"006698073LA042":
               {
                   "Nome":"cecilia muambumba",
                   "Cursos":["python","desenvolvimento web"],
                   "computador":"Mediateca"
                }
                    
}

aluna= base_de_dados.get(resultado)

if aluna:
    print("aluna foi encontrada com sucesso")

else:
    print("o BI não corresponde a nenhum documento")
