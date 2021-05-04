print('Calcular Índice de Massa Corporal - IMC')
print()
resp = 'S'
while resp == 'S':
    peso = float(input('Informe seu peso (kg): '))
    while peso < 1 or peso > 595: #595 foi o peso máximo que um ser humano atingiu.
        peso = float(input('Peso inválido, digite novamente: '))

    altura = float(input('Informe sua altura (m/cm): '))

    while altura <= 0 or altura > 2.72: #2.72 foi a altura máxima que um ser humano atingiu.
        altura = float(input('Altura inválida, digite novamente: '))

    imc = peso / altura ** 2
    print('O seu IMC é {:.2f}'.format(imc))
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc < 24.9:
        print('Peso normal')
    elif imc < 29.9:
        print('Sobrepeso')
    elif imc < 34.9:
        print('Obesidade grau I')
    elif imc < 39.9:
        print('Obesidade grau II')
    else:
        print('Obesidade Mórbida, cuidado!!!')
    resp = str(input('Calcular novamente (S / N)? ')).upper().strip()
    while resp != 'S' and resp != 'N':
        resp = str(input('Resposta inválida! Calcular novamente (S / N)? ')).upper().strip()
