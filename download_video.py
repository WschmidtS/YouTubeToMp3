from pytube import YouTube

link_youtube = input("Digite ou cole o link do vídeo para download:  ")
destino = input("Digite o caminho da pasta onde salvar o vídeo:  ")
youtube = YouTube(link_youtube)

print("Título: ", youtube.title)
print("Número de views: ", youtube.views)
print("Tamanho do vídeo: ", youtube.length, "segundos")
print("Avaliação do vídeo: ", youtube.rating)

video_download = youtube.streams.get_highest_resolution()

print("Fazendo o Download...")
video_download.download(destino)
print("Download completo com sucesso!")
