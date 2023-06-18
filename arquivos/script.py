from pathlib import Path # interagir com arquivos do pc
import shutil as sh # copiar arquivos e diretórios por completo

# ATUALIZANDO PASTA PYTHON

# Selecionando pasta Python do pc e do pen drive
file_py_pc = Path(r'C:\Users\mobishopgamer\Documents\Estudo\Hashtag\Python')
file_py_pd = Path(r'D:\Python')

# lista de caminhos dos arquivos da pasta Python no pc
list01_pc = [file for file in file_py_pc.iterdir()]
# lista com caminho e nome dos arquivos da pasta Python no pen drive
list01_pd = [file for file in file_py_pd.iterdir()]
list01_pd_name = [file.name for file in file_py_pd.iterdir()]

list02_pd_name = []

for archive_pd in list01_pd:
    list02_pd_name_add = [list02_pd_name.append(file.name) for file in archive_pd.iterdir() if file.is_dir() or file.is_file()]

# Percorrendo arquivos no pc na pasta python
for archive in list01_pc:
    # se o arquivo do pc não existir no pen drive:
    if not archive.name in list01_pd_name:
        # criar cópia do diretório inteiro para o pen drive
        sh.copytree(archive, rf'D:\Python\{archive.name}')

    list02_pc = [file for file in archive.iterdir() if file.is_dir() or file.is_file()]

    # arquivos existentes no pc e nao existentes no pen drive
    arquivos_backup = [file_noexist for file_noexist in list02_pc if not file_noexist.name in list02_pd_name]

    # Percorrendo subpastas da pasta Python
    for item in list02_pc:
        # criar cópia dos arquivos e diretórios (existentes apenas no pc) de subpastas para o pen drive
        if item in arquivos_backup:
            if item.is_file():
                sh.copy(item, rf'D:\Python\{archive.name}\{item.name}')
            elif item.is_dir():
                sh.copytree(item, rf'D:\Python\{archive.name}\{item.name}')

        # Criando código específico para a pasta Aulas/ArquivosAulas para criar cópias de arquivos e diretórios dentro dela não existentes no pen drive, já que criar uma cópia inteira desta pasta não foi possível por ela já existir
        elif item.name == 'ArquivosAulas':
            qntd_arquivos_pc = [file for file in item.iterdir() if file.is_dir() or file.is_file()]
            qntd_arquivos_pd = [file.name for file in Path(r'D:\Python\Aulas\ArquivosAulas').iterdir() if file.is_dir() or file.is_file()]

            if not len(qntd_arquivos_pc) == len(qntd_arquivos_pd):
                for new_item in qntd_arquivos_pc:
                    if not new_item.name in qntd_arquivos_pd:
                        if new_item.is_file():
                            sh.copy(new_item, rf'D:\Python\{archive.name}\{item.name}\{new_item.name}')
                        elif new_item.is_dir():
                            sh.copytree(new_item, rf'D:\Python\{archive.name}\{item.name}\{new_item.name}')

print('backup realizado com sucesso!')