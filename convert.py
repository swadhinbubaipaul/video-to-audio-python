import moviepy as mp
import os
import glob


def convert_mp4_to_mp3(video_file, mp3_folder):
    """
    Convert a single MP4 file to MP3 format.

    Args:
        video_file (str): Path to the input MP4 file
        mp3_folder (str): Directory where the MP3 file will be saved

    Returns:
        None
    """
    try:
        # Create video clip object from the input file
        clip = mp.VideoFileClip(video_file)

        # Generate output filename by replacing .mp4 extension with .mp3
        mp3_filename = os.path.basename(os.path.splitext(video_file)[0] + ".mp3")
        audio_file = os.path.join(mp3_folder, mp3_filename)

        # Extract audio from video and save as MP3
        clip.audio.write_audiofile(audio_file)

        # Close the clip to free up system resources
        clip.close()

        print(f"Successfully converted {video_file} to {audio_file}")
    except Exception as e:
        print(f"Error converting {video_file}: {str(e)}")


def main():
    """
    Main function that handles the batch conversion of MP4 files to MP3.
    - Sets up input/output directories
    - Finds all MP4 files in the input directory
    - Converts each file to MP3 format
    """
    # Define the source directory containing MP4 files
    path_to_mp4_files = "path/to/your/mp4/files"

    # Create a subdirectory for MP3 outputs
    mp3_folder = os.path.join(path_to_mp4_files, "mp3")

    # Ensure the output directory exists
    os.makedirs(mp3_folder, exist_ok=True)

    # Find all MP4 files in the source directory
    mp4_files = glob.glob(os.path.join(path_to_mp4_files, "*.mp4"))

    if not mp4_files:
        print("No MP4 files found in the directory!")
        return

    print(f"Found {len(mp4_files)} MP4 files to convert")
    print(f"MP3 files will be saved in: {mp3_folder}")

    # Process each MP4 file
    for video_file in mp4_files:
        convert_mp4_to_mp3(video_file, mp3_folder)


if __name__ == "__main__":
    main()
