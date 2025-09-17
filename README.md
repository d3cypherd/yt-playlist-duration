<div align="center">

# 🕒 YouTube Playlist Duration Calculator

Calculate the total duration of a **selected range** of YouTube playlist videos and displays the viewing time at **various playback speeds** (1x, 1.25x, 1.5x, 1.75x, 2x)

![overview](tutorial.webp)

</div>


## 📦 Features

- Retrieves playlist metadata using `yt-dlp`
- Displays duration of each video (with fallback for unknown durations)
- Calculates total playlist time at various playback speeds
- Allows selection of a subset of the playlist by index range

## 🚀 Usage

```bash
python app.py <playlist_url> <start_index> <end_index>
```

- `playlist_url`: Link to the YouTube playlist
- `start_index`: First video index (1-based)
- `end_index`: Last video index (inclusive)

### Example
```bash
python app.py https://youtube.com/playlist?list=XYZ 1 10
```

This will analyze videos 1 through 10 in the playlist.

## 📋 Requirements
- Python 3.6+
- yt-dlp

Install yt-dlp using pip:
```bash
pip install yt-dlp
```

## 📄 Sample Output
```
🎵 Playlist: My Favorite Tutorials
1. 0:12:34 — Video Title 1
2. 0:08:45 — Video Title 2
...

🕒 Total Playlist Duration:
 1x      2:30:10
 1.25x   2:00:04
 1.5x    1:40:06
 1.75x   1:25:46
 2x      1:15:05
