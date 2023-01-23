from sys import argv
from pytube import YouTube, Playlist

DOWNLOAD_FOLDER = "/home/pato/Videos/"

# Available templates: (playlisttitle) (videoname) (videoindex)
VIDEO_NAME_TEMPLATE = "(videoname)"
# Available templates: (title)
PLAYLIST_TITLE_TEMPLATE = "(title)"

def download_playlist(playlist_url = ''):
    if playlist_url.strip() == '': playlist_url = input('Playlist url: ')

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

Extra:
    > Playlist size:  {playlist.length} videos
    > Playlist owner: {playlist.owner}
''')

    if input('Start download? (Y/n) ').lower() or 'y' == 'n': exit()

    index = 0
    for video_url in playlist:
        index += 1

        try:
            yt_obj = YouTube(video_url)
            video_name = VIDEO_NAME_TEMPLATE.replace('(playlisttitle)', playlist_title).replace('(videoname)', yt_obj.title.replace(' ', '')).replace('(videoindex)', str(index))
        except:
            print(f'[ERRO] Could not load video: {video_url}')
            continue

        print(f'[INFO] Downloading {video_name}.mp3 ({video_url})')

        try:
            yt_obj.streams.get_audio_only().download(output_path=f'{DOWNLOAD_FOLDER}{playlist_title}/', filename=f'{video_name}.mp3')
            print(f'[DONE] Downloaded at: {DOWNLOAD_FOLDER}{playlist_title}/{video_name}.mp3')
        except:
            print(f'[ERRO] Could not download: {video_name} ({video_url})')

def download_video(video_url = ''):
    if video_url.strip() == '': video_url = input('Video url: ')

    try:
        yt_obj = YouTube(video_url)
        video_name = VIDEO_NAME_TEMPLATE.replace('(playlisttitle)', '').replace('(videoname)', yt_obj.title.replace(' ', '')).replace('(videoindex)', '')
    except:
        print(f'[ERRO] Could not load video: {video_url}')
        exit()

    print(f'''About:
    > Video title:   {yt_obj.title}
    > Playlist url:  {video_url}
    > Output folder: {DOWNLOAD_FOLDER}

Formatting:
    > Video name template: {VIDEO_NAME_TEMPLATE}

Extra:
    > Video author: {yt_obj.author}
''')

    if input('Start download? (Y/n) ').lower() or 'y' == 'n': exit()

    print(f'[INFO] Downloading {video_name}.mp3 ({video_url})')

    try:
        yt_obj.streams.get_audio_only().download(output_path=f'{DOWNLOAD_FOLDER}', filename=f'{video_name}.mp3')
        print(f'[DONE] Downloaded at: {DOWNLOAD_FOLDER}{video_name}.mp3')
    except:
        print(f'[ERRO] Could not download: {video_name} ({video_url})')

args = argv
args.pop(0)

if len(args) == 0:
    # TODO: Create a help menu
    print('usage: ytdp playlist or ytdp video')
    exit()

command = args[0]
url = '' if len(args) < 2 else args[1]

if command == 'playlist' or command == 'p': download_playlist(url)
if command == 'video'    or command == 'v': download_video(url)
