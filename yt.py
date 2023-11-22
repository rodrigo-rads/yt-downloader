import pytube

def download_playlist(url):
  playlist = pytube.Playlist(url)
  for url in playlist.video_urls:
    resolution = 22
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(resolution)
    stream.download()
    return stream.default_filename