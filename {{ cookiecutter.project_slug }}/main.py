from datetime import datetime, timedelta

from src import generacion_bases

dia = int(str(datetime.now()).replace('-', '')[:8])
mes = int(str(datetime.now()).replace('-', '')[:6])

def main():
    print('Hello World')

    generacion_bases.run(dia)

if __name__ == '__main__':
    main()