# ytdownloader

A simple python script for downloading playlist (as .mp3).  
> Made for linux (might work on Windows after patching)

## Build

```bash
git clone https://github.com/devkcud/ytdownloader.git
cd ytdownloader
```

**ATTENTION:** Before running the script or running `make`, change the _DOWNLOAD_FOLDER_ at [ytd.py](ytd.py) to a directory that exists on your system, otherwise it won't download correctly (might break).

After patching, you can install locally or in the binaries folder (_/usr/local/bin_).

System:
```bash
make
# or
make install
```

Local:
```bash
make transform
./ytdp
```

To delete the script run:
```bash
make clean # Local
make uninstall # System
```

## Configuration

You can change the _VIDEO_NAME_TEMPLATE_ and _PLAYLIST_TITLE_TEMPLATE_ variables inside the [ytd.py](ytd.py).

Example _VIDEO_NAME_TEMPLATE_:
```python
VIDEO_NAME_TEMPLATE = "(videoname)"
VIDEO_NAME_TEMPLATE = "video-(videoindex)"
VIDEO_NAME_TEMPLATE = "this_is_my_(videoindex)_audio_file"
VIDEO_NAME_TEMPLATE = "(playlisttitle)-video(videoindex)"
```

Example _PLAYLIST_TITLE_TEMPLATE_:
```python
PLAYLIST_TITLE_TEMPLATE = "(title)"
PLAYLIST_TITLE_TEMPLATE = "OST_(title)"
PLAYLIST_TITLE_TEMPLATE = "(title)-musics"
PLAYLIST_TITLE_TEMPLATE = "CustomFolderName"
```

## Disclaimer

- I am **NOT** a python developer;
- I am **NOT** familiar with _Makefiles_;
- I just wanted to create something that I can use.

## License

This project is under the [The Unlicense](LICENSE) license.
