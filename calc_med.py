A = 5
B = 15
C = 20
D = 30
E = 45

idade =  int(input("Digite sua idade:"))

if idade >=18:
    print("maior de idade")
else:
    print("menor de idade")
notaA = float(input("Informe a priemira nota:"))
notaB = float(input("informe a segunda nota:"))

mediafinal = (notaA + notaB) / 2

if mediafinal >+ 7.0:
    print("A Média : %.1f - Aprovado" % mediafinal)
else:
    print("A Média: %.1f - Reprovado"% mediafinal)
