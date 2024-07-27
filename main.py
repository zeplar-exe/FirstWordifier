import sys
import uuid

from library import first_wordify

target_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) >= 3 else f"out{uuid.uuid1()}.mp4"
language = sys.argv[3] if len(sys.argv) >= 4 else "en"
model = sys.argv[4] if len(sys.argv) >= 5 else "base"

first_wordify(target_file, language, output_file, model)