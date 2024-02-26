# Save_Paint
Script for saving images in paint

# PT-br 

Descrição:
O Paint Saver é uma aplicação em Python que automatiza o processo de abrir imagens no Paint, faz alguma edição (salva a imagem), e fecha o Paint.

Instruções de Uso:

Execute o programa Python.
Selecione a pasta contendo as imagens que você deseja processar.
Aguarde enquanto o programa abre cada imagem no Paint e faz as edições programadas.
Ao finalizar, o programa exibirá a mensagem "Programa finalizado!".

Motivo da Criação:
Este programa foi desenvolvido para resolver um problema específico. Ao baixar diversas imagens de vários sites e posteriormente abrir 
essas imagens no programa Adobe Premiere, percebi que elas vinham corrompidas. 
No entanto, ao abrir a imagem no Paint e salvá-la novamente, a imagem voltava ao seu estado normal. 
Este programa automatiza esse processo de abertura e salvamento, poupando tempo e esforço.

Requisitos:

Python 3.x instalado
Bibliotecas: os, time, pyautogui, subprocess, tkinter
Configuração:

Certifique-se de ter o Python instalado em seu sistema.
Instale as bibliotecas necessárias usando o seguinte comando:
bash
Copy code
pip install pyautogui tk
Observações:

O caminho para o executável do Paint deve ser ajustado conforme necessário (caminho_paint no código).
Certifique-se de fornecer permissões adequadas para acessar e modificar os arquivos na pasta selecionada.
Importante:

Este programa é fornecido sem garantias de qualquer tipo. Use por sua própria conta e risco.
