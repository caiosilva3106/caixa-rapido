def somar (valor_principal, acrescimo):
    '''
    Adiciona o acrescimo ao valor pricipal

    Arg:
        valor_principal (float):valor inicil da soma
        acrescimo (float):valor a ser adicinado a valor inicial

        Returnns
            float:somado do valor principal e acrescimo
    '''
    return valor_principal + acrescimo

def testar_operacao_soma():
    # Arrage
    valor1=100.0
    valor2=50.0
    # Act
    resultado =somar(valor1 ,valor2)
    # Assert
    assert resultado ==150.0, "A soma falhou!"
    print("Tete de soma: PASSOU!")

testar_operacao_soma()