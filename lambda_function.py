import json
from log import log

def lambda_handler(event, context):
    log(f"event {json.dumps(event)}")
    return {
        'statusCode': 200,
        'body': f'<html><body>Dados da requisicao {event}</body></html>',
        'headers': {
            "content-type": "text/html"
        }
    }

# import json
# import logging
# import boto3
# from log import log
# from botocore.exceptions import ClientError
# def lambda_handler(event, context):
#     s3_name = event['Records'][0]['s3']['bucket']['name']
#     s3_key = event['Records'][0]['s3']['object']['key']
    
#     print(s3_name,s3_key)
#     # Recupere o objeto S3 usando o nome do objeto e o bucket S3
#     s3_client = boto3.client('s3')
#     s3_object = s3_client.get_object(Bucket=s3_name, Key=s3_key)
    
#     # Carregue o conteúdo do objeto S3 como JSON
#     json_content = s3_object['Body'].read().decode('utf-8')
#     json_data = json.loads(json_content)
#     print(json_data)
#     return {
#         'statusCode': 200,
#         'body': f'<html><body>Dados da requisicao {event}</body></html>',
#         'headers': {
#             "content-type": "text/html"
#         }
#     }