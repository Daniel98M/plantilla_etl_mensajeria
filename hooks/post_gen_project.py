"Script to run after the project is generated"
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f'{MESSAGE_COLOR}Ya casi hemos terminado.{RESET_ALL}')

# Inicializar un repositorio en git
print(f'{MESSAGE_COLOR}Inicializando repositorio de git.{RESET_ALL}')

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'chore ⚒️: First commit'])

# Creación del entorno virtual
ENV_MANAGER = '{{ cookiecutter.environment_manager }}'.lower()

if ENV_MANAGER == 'virtualenv':
    print(f'{MESSAGE_COLOR}Creando entorno virtual con virtualenv.{RESET_ALL}')
    subprocess.call(['python', '-m', 'venv', 'venv'])

elif ENV_MANAGER == 'poetry':
    print(f'{MESSAGE_COLOR}Creando entorno virtual con poetry.{RESET_ALL}')
    subprocess.call(['poetry', 'init', '-n'])

else:
    print(f'{MESSAGE_COLOR}Sin entorno virtual. Puedes crearlo más tarde si lo deseas.{RESET_ALL}')

print(f'{MESSAGE_COLOR}Proyecto generado con éxito.{RESET_ALL}')
