import datetime
import sys

import yt_dlp

start = 0
end = -1
# Example usage: python app.py https://youtube.com/playlist?list=XYZ 1 10
playlist_url = sys.argv[1]
if len(sys.argv) >= 3:
    start = int(sys.argv[2]) - 1  # Convert to 0-based index
if len(sys.argv) >= 4:
    end = int(sys.argv[3])


# yt-dlp options to fetch metadata only
options = {
    "quiet": True,
    "extract_flat": True,
    "dump_single_json": True,
}

with yt_dlp.YoutubeDL(options) as ydl:
    info = ydl.extract_info(playlist_url, download=False)

    print(f"\n🎵 Playlist: {info['title']}")
    videos = info["entries"][start:end]

    total_length = 0
    for idx, video in enumerate(videos, start=start + 1):
        title = video.get("title", "N/A")
        duration = video.get("duration")  # in seconds

        # Print duration in mm:ss or fallback
        if duration is not None:
            formatted = str(datetime.timedelta(seconds=duration))
            total_length += duration
        else:
            formatted = "??:??"

        print(f"{idx}. {formatted} — {title}")

    # Final total duration formatting
    total_formatted_1x = str(datetime.timedelta(seconds=total_length))
    total_formatted_125x = str(datetime.timedelta(seconds=total_length // 1.25))
    total_formatted_15x = str(datetime.timedelta(seconds=total_length // 1.5))
    total_formatted_175x = str(datetime.timedelta(seconds=total_length // 1.75))
    total_formatted_2x = str(datetime.timedelta(seconds=total_length // 2))
    print("\n🕒 Total Playlist Duration:")
    print(f" {'1x':<6} {total_formatted_1x:>10}")
    print(f" {'1.25x':<6} {total_formatted_125x:>10}")
    print(f" {'1.5x':<6} {total_formatted_15x:>10}")
    print(f" {'1.75x':<6} {total_formatted_175x:>10}")
    print(f" {'2x':<6} {total_formatted_2x:>10}")
