import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith('x'):
    print(f'{ERROR_COLOR}ERROR: {project_slug=} no es un nombre valido.{RESET_ALL}')
    
    sys.exit(1)

print(f'{MESSAGE_COLOR}Creando proyecto...{RESET_ALL}')