from pytube import YouTube
import moviepy.editor
import re
import os

link_youtube = input('Digite ou cole o link do vídeo para download:')
destino = input('Digite o caminho da pasta onde salvar os arquivos:')
youtube = YouTube(link_youtube)

print('Fazendo o Download do Vídeo')
print('Aguarde ...')
video_download = youtube.streams.filter(only_audio=True).first().download(destino)
print('Download completo!')

print('Convertendo arquivo para MP3')
print('Aguarde ...')

for video_baixado in os.listdir(destino):
    if re.search('mp4', video_baixado):
        video = os.path.join(destino, video_baixado)
        arq_mp3 = os.path.join(destino, os.path.splitext(video_baixado)[0] + '.mp3')
        new_file = moviepy.editor.AudioFileClip(video)
        new_file.write_audiofile(arq_mp3)
        os.remove(video)
print('Sucesso!')
