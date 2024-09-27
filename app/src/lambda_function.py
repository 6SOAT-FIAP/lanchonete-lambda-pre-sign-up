# Acionador lambda para validações no pré-cadastro

def lambda_handler(event, context):

    event['response']['autoConfirmUser'] = True

    cpf = event['userName']
    
    if not cpf.isdigit() or len(cpf) != 11:
        raise Exception("O CPF nao e valido")

    return event