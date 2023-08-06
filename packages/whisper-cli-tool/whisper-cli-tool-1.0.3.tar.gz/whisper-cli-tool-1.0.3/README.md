Whisper CLI
================
CLI to translate an audiofile on the command-line

## Setup

Before to install, make sure you have a OpenAI api key available on your computer PATH.

Execute the command below to install the `whisper-cli-tool` python package, which offer the `whisper` command line utility to make transcriptions.

```bash
$ pip install whisper-cli-tool
```

After installation, just execute:

```bash
$ whisper --help

usage: whisper [-h] [--response-format RESPONSE_FORMAT] [--language LANGUAGE] [--outfile OUTFILE] infile

Do transcription of an audiofile

positional arguments:
  infile                Input file name. Supported formats: m4a, mp3, webm, mp4, mpga, wav, mpeg.

options:
  -h, --help            show this help message and exit
  --response-format RESPONSE_FORMAT
                        Response format. Supported formats: text, srt.
  --language LANGUAGE   Language the audio should be translated to
  --outfile OUTFILE     Output file name
```

## Usage

To transcribe an audio to portuguese in text format, just execute:
```
$ whisper my-audio.mp3
```
where my-audio.mp3 is your audiofile. The transcribed text will be saved into transcription-output.txt 

If you want to change arguments, let's say, change the response format from text to str, just do:
```
$ whisper my-audio.mp3 --response-format str --language pt --outfile my-transcription.mp3
```
