"""This snippet will guide you to download a streaming media.

Ensure you have the required Python libraries installed. You'll need the requests library for HTTP requests, ffmpeg-python for multimedia handling, cryptography for decryption (if required), and m3u8 for parsing M3U8 files.

Install the libraries via pip:
#! pip install requests ffmpeg-python cryptography m3u8
"""
import subprocess

import requests
from m3u8 import M3U8


def decrypt_segment(segment_content, m3u8_parser):
    # key = ... # Extract the key from the M3U8 file
    # iv = ... # Extract the IV (Initialization Vector) from the M3U8 file
    # cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # decryptor = cipher.decryptor()
    # decrypted_segment = decryptor.update(segment_content) + decryptor.finalize()
    return segment_content


def download_media(streaming_url):
    # Fetch the M3U8 File
    response = requests.get(streaming_url)
    if response.status_code == 200:
        m3u8_content = response.text
    else:
        print("Failed to fetch M3U8 file")
        return

    # Parse and Extract Segment URLs
    parser = M3U8()
    parser.read(m3u8_content)
    segment_urls = parser.segments.uri

    # Download HLS Segments
    # Iterate through segment URLs and download each segment
    segment_output_fnames = []
    for index, segment_url in enumerate(segment_urls):
        segment_response = requests.get(segment_url)
        if segment_response.status_code == 200:
            segment_content = segment_response.content
            # Decrypt Segment Content (Optional)
            # segment_content = decrypt_segment(segment_content, m3u8_parser)
            # Save the segment locally (adjust file naming and storage as needed)
            output_fname = f"segment_file_{index}.ts"
            segment_output_fnames.append(output_fname)
            with open(output_fname, "wb") as segment_file:
                segment_file.write(segment_content)
        else:
            print(f"Failed to download segment: {segment_url}")

    # Merge Segments (Optional)
    # Example merging segments using FFMPEG
    combined_segment_fnames = "|".join(segment_output_fnames)
    subprocess.call(
        f'ffmpeg -i "concat:{combined_segment_fnames}" -c copy output.mp4',
        shell=True,
    )

    print("Done.")
