import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f'{MESSAGE_COLOR}Ya casi hemos terminado.{RESET_ALL}')

# Inicializar un repositorio en git
print(f'{MESSAGE_COLOR}Inicializando repositorio de git.{RESET_ALL}')

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'First commit'])

print(f'{MESSAGE_COLOR}Proyecto generado con éxito.{RESET_ALL}')
