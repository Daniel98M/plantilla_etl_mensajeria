import pandas as pd
import numpy as np

from Utils.functions import send_message, config_logging

def run(dia, config):
    logger = config_logging(dia)
    logger.info('Ejecutando generación de bases')

    print(f'Ejecutando generación de bases el {dia}')
    print(config)

if __name__ == '__main__':
    run()