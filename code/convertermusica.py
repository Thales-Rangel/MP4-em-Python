from pathlib import Path
import os
import yt_dlp


def download_music():
    with open(r"_Caminho_de_um_arquivo_de_texto_com_os_links_das_músicas_no_Youtube") as musicas_txt:
        for linha in musicas_txt:
            link = linha
            path = (r"_Diretório_para_onde_as_músicas_vão_")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': r'C:\Users\thale\OneDrive\Documentos\ffmpeg\ffmpeg-master-latest-win64-gpl-shared\bin',
            }
            #Fazer o dowload

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print("Download completo")
            
download_music()