# This is a sample Python script.
import argparse
import logging
import os

import bibtexparser
from pyzotero.zotero import Zotero


def main():
    args = get_args()
    sync(**vars(args))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("sync",))
    parser.add_argument("library_type", choices=("library", "group"))
    parser.add_argument("library_id")
    parser.add_argument("out_file")
    parser.add_argument("--api-key",
                        required=True,
                        default=os.environ.get("ZOTERO_API_KEY", None),
                        help="Provide Zotero API key with --api-key or environment variable $ZOTERO_API_KEY",
    )
    parser.add_argument("--log-level", choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"), default="INFO")
    return parser.parse_args()


def sync(action, library_id, out_file, library_type, api_key, log_level):
    logging.basicConfig(level=log_level)
    logging.info(f"Retrieving library...")
    library = Zotero(library_id, library_type, api_key)
    write_bibtex(library, out_file)
    logging.info(f"Wrote file to {out_file}")


def write_bibtex(library, out_file):
    bibtex_database = library.items(format="bibtex")
    if "/" in out_file:
        os.makedirs(os.path.dirname(out_file), exist_ok=True)

    with open(out_file, "w") as f:
        bibtexparser.dump(bibtex_database, f)



if __name__ == '__main__':
    main()
