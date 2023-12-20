import argparse
import asyncio
import os
from pathlib import Path
import sys
import time
from pydub import AudioSegment
from pydub.playback import play


async def _print_time_passed(start: int):
    assert start > 0

    for remaining in range(start, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        await asyncio.sleep(1)
    os.system("clear")


async def _entry():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int)
    parser.add_argument("endsound", type=Path)
    args = parser.parse_args()

    await _print_time_passed(args.start)

    print("CHILL TIME")
    bellsound = AudioSegment.from_file(args.endsound)
    play(bellsound)


def main():
    asyncio.run(_entry())


if __name__ == "__main__":
    main()
