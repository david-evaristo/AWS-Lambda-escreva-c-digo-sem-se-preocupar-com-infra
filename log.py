import logging
import json
import os
  

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def log(mensagem):
    logger.info(os.environ['MINHA_VAR'])
    log = logger.info(mensagem)
    return log