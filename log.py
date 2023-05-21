import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def log(mensagem):
    log = logger.info(f'Adicionando log via função: {mensagem}')
    return log