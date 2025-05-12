# MP4 to MP3 Converter

A Python script that converts MP4 video files to MP3 audio files. This tool is perfect for extracting audio from video files in batch mode.

## Features

-   Converts multiple MP4 files to MP3 format
-   Processes all MP4 files in a specified directory
-   Creates a separate output folder for MP3 files
-   Provides progress feedback during conversion
-   Handles errors gracefully

## Requirements

-   Python 3.x
-   moviepy library
-   FFmpeg

## Installation

1. First, ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install FFmpeg:

    - **Windows**:
        - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
        - Extract the downloaded file
        - Add FFmpeg to your system's PATH environment variable
    - **Mac** (using Homebrew):
        ```bash
        brew install ffmpeg
        ```
    - **Linux**:
        ```bash
        sudo apt-get update
        sudo apt-get install ffmpeg
        ```

3. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/mp4-to-mp3-converter.git
    cd mp4-to-mp3-converter
    ```

4. Install the required Python packages:
    ```bash
    pip install moviepy
    ```

## Usage

1. Open `convert.py` and modify the `path_to_mp4_files` variable to point to your directory containing MP4 files:

    ```python
    path_to_mp4_files = "path/to/your/mp4/files"
    ```

2. Run the script:
    ```bash
    python convert.py
    ```

The script will:

-   Create an 'mp3' subdirectory in your specified path
-   Convert all MP4 files in the directory to MP3 format
-   Save the converted files in the 'mp3' subdirectory
-   Display progress information during conversion

## Output

-   Converted MP3 files will be saved in an 'mp3' subdirectory
-   Each MP3 file will have the same name as its corresponding MP4 file
-   The script provides feedback for each successful conversion and any errors

## Error Handling

The script includes error handling for common issues:

-   Missing input files
-   Invalid file formats
-   Conversion errors
-   File system errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

-   [moviepy](https://zulko.github.io/moviepy/) library for video processing
-   [FFmpeg](https://ffmpeg.org/) for media handling

## Support

If you encounter any problems or have any suggestions, please open an issue on GitHub.
