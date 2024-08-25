import importlib.metadata as metadata
import logging
import signal
import sys
from typing import Any
import argparse


def get_version() -> str:
    try:
        return str(metadata.version("linuxtag"))
    except metadata.PackageNotFoundError:
        return "0.0"


def handler(signum: int, frame: Any) -> None:
    print("Exiting...")
    sys.exit(0)


def init_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)8s] %(asctime)s %(funcName)10s : %(message)s",
        handlers=[
            logging.StreamHandler(),
        ],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", default=False)
    args = parser.parse_args()

    if args.test:
        print("ok")
        return

    # handle keyboard interrupts
    signal.signal(signal.SIGINT, handler)

    init_logging()

    print("Hello!")
    logging.info("Hello!")
    print(get_version())


if __name__ == "__main__":
    main()
