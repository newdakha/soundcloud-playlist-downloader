import yt_dlp

def download_soundcloud_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': False,
        'cookiesfrombrowser': ('firefox',), # or 'chrome', 'brave', 'opera' . . .
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    download_soundcloud_playlist("https://soundcloud.com/newdakha/")
