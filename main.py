import yt

link = input("Cole o link da playlist: ")
print("Downloading...")
yt.download_playlist(link)
print("Finalizado.")

