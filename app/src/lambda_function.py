# Acionador lambda para pré-cadastro

def lambda_handler(event, context):

    event['response']['autoConfirmUser'] = True

    cpf = event['userName']
    
    if not cpf.isdigit() or len(cpf) != 11:
        raise Exception("O CPF não é válido")

    return event