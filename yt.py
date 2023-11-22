import pytube

def download_playlist(playlist_url):
  playlist = pytube.Playlist(playlist_url)
  for url in playlist.video_urls:
    download_video(url)
  
def download_video(url):
  resolution = 22 # 720p
  video = pytube.YouTube(url)
  stream = video.streams.get_by_itag(resolution)
  stream.download('downloads')
  return stream.default_filename