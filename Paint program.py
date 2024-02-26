import os
import time
import pyautogui
import subprocess
import tkinter as tk
from tkinter import filedialog

print('\n----- PROGRAM SAVE IMAGES IN PAINT -----\n')


# Função que seleciona a pasta de imagens
def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        print(f"Pasta selecionada: {pasta_selecionada}")

        # Chama a função do programa
        save_images(pasta_selecionada)

# Função que salva as imagens
def save_images(pasta_selecionada):
    # Caminho para o executável do Paint
    caminho_paint = r'C:\Users\jotag\AppData\Local\Microsoft\WindowsApps\mspaint.exe'

    # Obter a lista de arquivos na pasta de fotos
    arquivos_na_pasta = os.listdir(pasta_selecionada)

    # Filtrar apenas os arquivos em PNG
    arquivos_png = [arquivo for arquivo in arquivos_na_pasta if
                    (arquivo.lower().endswith('.jpg') or arquivo.lower().endswith('.png'))]

    print(arquivos_na_pasta)

    for idx, foto in enumerate(arquivos_png):
        print('Arquivos a serem salvos:', len(arquivos_png) - idx)

        # Escolher o arquivo PNG/JPEG
        nome_arquivo_png = os.path.join(pasta_selecionada, foto)

        # Abrir a foto no Paint
        subprocess.Popen([caminho_paint, nome_arquivo_png])

        # Aguardar um momento para garantir que o Paint esteja aberto
        time.sleep(2)

        # Salvar a imagem
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)

        # Fechar o Paint
        pyautogui.hotkey('alt', 'f4')

        print(f'Arquivo alterado: {foto}\n')
    print('Arquivos Salvos!')

    janela.update()

# Função de finalização do programa
def evento_final():

    texto_final = tk.Label(janela, text="Programa finalizado!")
    texto_final.pack()


if __name__ == '__main__':
    # Criar a janela principal do programa
    janela = tk.Tk()
    janela.title("Programa: Paint Saver")

    window_width = 500
    window_height = 200

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    janela.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    texto = tk.Label(janela, text="Selecione a pasta desejada:")

    texto.pack()

    # Criar um botão para selecionar a pasta
    botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=lambda: [selecionar_pasta(), evento_final()])
    botao_selecionar.pack(pady=20)

    # Iniciar o loop principal da interface gráfica
    janela.mainloop()

print('Programa finalizado com sucesso!')
