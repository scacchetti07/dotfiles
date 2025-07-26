# Script em python para mover todos os arquivos das pastas para o diretório .config + seu nome ('.config/dir_name')

import os

path = '/run/media/scacchetti/HD/dotfiles' # Meu path para o diretório dotfile
dir = os.listdir(path)

for e in dir:
    if e == '.git':
        continue

    complete_path = f'{path}/{e}'
    try:
        files = os.listdir(complete_path)
        if os.path.exists(f'{path}/{e}/.config'):
            print(f'Já exite \'.config/\'no diretório {e}')
            continue
        print(f'Movendo arquivos de \'{e}\'')

        # Criando pastas .config
        os.mkdir(f'{complete_path}/.config')
        os.mkdir(f'{complete_path}/.config/{e}')

        # Movendo arquivos
        for f in files:
            os.replace(f'{complete_path}/{f}', f'{complete_path}/.config/{e}/{f}')
    except NotADirectoryError:
        continue;
print('Completo! O Script foi executado com Sucesso!')
