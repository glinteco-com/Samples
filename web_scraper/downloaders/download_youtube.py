from pathlib import Path

import ffmpeg
from pytube import YouTube

links = [
    "https://www.youtube.com/watch?v=6zTc2hD2npA&ab_channel=AucklandSymphonyOrchestra",
    "https://www.youtube.com/watch?v=UDVtMYqUAyw&ab_channel=Cin%C3%A9mavore",
    "https://www.youtube.com/watch?v=NBE-uBgtINg&ab_channel=HDFilmTributes",
    "https://www.youtube.com/watch?v=F2RnxZnubCM&ab_channel=HDFilmTributes",
    "https://www.youtube.com/watch?v=p0MdP8KeAII&ab_channel=HDFilmTributes",
    "https://www.youtube.com/watch?v=va1oiojnGrA&ab_channel=KlayaR__",
    "https://www.youtube.com/watch?v=3yBgLxgwS1U&ab_channel=smarTVirus"
    "https://www.youtube.com/watch?v=d_HlPboLRL8&ab_channel=iamAURORAVEVO",
]

output_path = "/Users/joe/Music/Downloads"
for link in links:
    print(link)
    yt = YouTube(link)
    download_file = (
        yt.streams.filter(progressive=True)
        .order_by("resolution")
        .desc()
        .first()
        .download(output_path=output_path)
    )
    stream = ffmpeg.input(download_file)
    audio = stream.audio
    file_name = Path(download_file)
    filename_wo_ext = file_name.with_suffix("")
    filename_replace_ext = file_name.with_suffix(".mp3")
    stream = ffmpeg.output(audio, str(filename_replace_ext))
    ffmpeg.run(stream, overwrite_output=1)
    print("---------------------------")
