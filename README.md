# FirstWordifier

Quick script I threw together to make somewhat entertaining edits of videos.

To install, download and unpack the repository.

Before using, make sure to `pip install -r requirements.txt`. [ffmpeg](https://www.ffmpeg.org/download.html) is additionally required for audio stuffs.

Program can be used like so

```shell
python main.py <input-file> [output-file] [language-code] [model] # no argparser, sorry
```

For model choices, see [available whisper models](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages). Be mindful of how much memory is available on your system.