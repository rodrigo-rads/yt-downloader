import yt

print('''
  Baixar videos do YT
  Selecione uma das opções abaixo:
  
  1 - Baixar uma playlist
  2 - Baixar um vídeo
''')

opcao = int(input("Opção: "))

if opcao == 1:
  link = input("Cole o link da playlist: ")
  print("Downloading...")
  yt.download_playlist(link)
  print("Finalizado.")

elif opcao == 2:
  link = input("Cole o link do video: ")
  print("Downloading...")
  yt.download_video(link)
  print("Finalizado.")

else:
  print("Opção inválida.")
