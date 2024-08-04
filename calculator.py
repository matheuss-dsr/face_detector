while True:  
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite um número: "))
    #operações
    soma = n1 + n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    subtracao = n1 - n2
    elevado = n1**n2
    operacao = input("Digite uma operação: ")
    if (operacao == '+'):
        resultado = soma
        print(n1, operacao, n2, '=', resultado)
    elif(operacao == 'x'):
        resultado = multiplicacao
        print(n1, operacao, n2, '=', resultado)
    elif(operacao == '/'):
        resultado = divisao
        print(n1, operacao, n2, '=', resultado)
    elif(operacao == '-'):
        resultado = subtracao
        print(n1, operacao, n2, '=', resultado)
    elif(operacao == '^'):
        resultado = elevado
        print(n1, operacao, n2, '=', resultado)
    else:
        print("Operação não castrada!")