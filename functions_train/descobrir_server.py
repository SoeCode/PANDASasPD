def descobrir_servidor(email):
    '''Descobre o servidor de email do usuário
    
    Parameters:
        um input com o email
    Return:
        Servidor de email utilizado
     '''
    try:
        posicao_a = email.index('@')
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'O servidor é gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'
    except:
        raise Exception('@ não encontrado, preencha novamente.')
    

email = input('DIGITE SEU EMAIL: ')
print(descobrir_servidor(email))