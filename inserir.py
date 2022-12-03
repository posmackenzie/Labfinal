import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamo')

tabela = dynamodb.Table('webservicepos')

now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def handler(event, context):
    cpf = event['cpf']
    nome = event['nome']

    response = tabela.put_item(
        Item = {
            'CPF': cpf,
            'NOME': nome
        }
    )
    return{
        'statusCode': 200,
        'body': json.dumps('Nome do cliente: ' + nome)
    }