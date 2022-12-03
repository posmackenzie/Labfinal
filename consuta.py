import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamo')

tabela = dynamodb.Table('webservicepos')

def handler(event, context):
    cpf = event['cpf']
    try:
        response = tabela.get_item(
            Key = {
                'CPF': cpf,
            }, ProjectionExpression = 'NOME'
        )
        nome = response['Item']['NOME']
    except ClientError as e:
        retorno = e.response['Error']['Message']

    return{
            'statusCode': 200,
            'body': json.dumps('Nome do cliente: ' + nome)
        }