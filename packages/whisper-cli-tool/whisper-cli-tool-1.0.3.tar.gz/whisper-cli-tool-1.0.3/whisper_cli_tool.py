import os
import openai
import argparse

def get_cli_args():
    USAGE = 'Do transcription of an audiofile'
    parser = argparse.ArgumentParser(description=USAGE)
    parser.add_argument('infile', 
                        type=str,
                        help='Input file name. Supported formats: m4a, mp3, webm, mp4, mpga, wav, mpeg.')
    parser.add_argument('--response-format', 
                        type=str, 
                        default='text', 
                        help='Response format. Supported formats: text, srt.')
    parser.add_argument('--language', 
                        type=str, 
                        default='pt',
                        help='Language the audio should be translated to')
    parser.add_argument('--outfile', 
                        type=str,
                        default='transcription-output.txt',
                        help='Output file name')
    args = parser.parse_args()

    return args

def main():
    args = get_cli_args()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    with open(args.infile, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file = audio_file,
            model = "whisper-1",
            response_format=args.response_format,
            language=args.language
        )

    with open(args.outfile, "w") as text_file:
        text_file.write(transcript)

if __name__ == '__main__':
    main()