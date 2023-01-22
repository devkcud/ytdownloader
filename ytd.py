from pytube import YouTube, Playlist

DOWNLOAD_FOLDER = "/home/pato/Videos/"

# Available templates: (playlisttitle) (videoname) (videoindex)
VIDEO_NAME_TEMPLATE = "(playlisttitle)_(videoindex)"
# Available templates: (title)
PLAYLIST_TITLE_TEMPLATE = "(title)"

def download_playlist(playlist_url = ''):
    if playlist_url == '': playlist_url = input('Playlist url: ')

    try:
        playlist = Playlist(playlist_url)
    except:
        print(f'Could not get playlist. URL: {playlist_url}')
        exit(1)

    playlist_title_normal = playlist.title
    playlist_title = PLAYLIST_TITLE_TEMPLATE.replace('(title)', playlist_title_normal.title().replace(" ", ""))

    print(f'''About:
    > Playlist title: {playlist_title_normal}
    > Playlist url:   {playlist_url}
    > Output folder:  {DOWNLOAD_FOLDER}{playlist_title}/

Formatting:
    > Playlist title template: {PLAYLIST_TITLE_TEMPLATE}
    > Video name template: {VIDEO_NAME_TEMPLATE}

Sizing:
    > Playlist videos quantity: {len(playlist)}
''')

    if input('Start download? (Y/n) ').lower() or 'y' == 'n': exit()

    index = 0
    for video_url in playlist:
        index += 1

        ytObj = YouTube(video_url)
        video_name = VIDEO_NAME_TEMPLATE.replace('(playlisttitle)', playlist_title).replace('(videoname)', ytObj.title.replace(' ', '')).replace('(videoindex)', str(index))

        print(f'[INFO] Downloading {video_name}.mp3 ({video_url})')

        try:
            ytObj.streams.get_audio_only().download(output_path=f'{DOWNLOAD_FOLDER}{playlist_title}/', filename=f'{video_name}.mp3')
            print(f'[DONE] Downloaded at: {DOWNLOAD_FOLDER}{playlist_title}/{video_name}.mp3')
        except:
            print(f'[ERRO] Could not download: {video_name} ({video_url})')

download_playlist('https://www.youtube.com/playlist?list=PLhWBaV_gmpGXxscZr8PIcreyYkw8VlnKn')
