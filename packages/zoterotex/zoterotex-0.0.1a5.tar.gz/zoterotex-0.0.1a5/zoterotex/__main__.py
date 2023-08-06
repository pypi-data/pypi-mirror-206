import argparse
import logging
import os
import re

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
    parser.add_argument("--api-key", default=os.environ.get("ZOTERO_API_KEY", None))
    parser.add_argument("--log-level", choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"), default="INFO")
    return parser.parse_args()


def sync(action, library_id, out_file, library_type, api_key, log_level):
    logging.basicConfig(level=log_level)
    if not api_key:
        raise ValueError("Must provide Zotero API key with --api-key or environment variable $ZOTERO_API_KEY")
    logging.info(f"Retrieving library...")
    library = Zotero(library_id, library_type, api_key)
    write_bibtex(library, out_file)


def write_bibtex(library, out_file):
    params = {}
    version = get_file_version(out_file, library.library_id)
    if version:
        params["since"] = version

    bibtex_database = library.items(format="bibtex", **params)
    if not bibtex_database:
        logging.info(f"No updates since version {version}. Quitting.")
        return

    if "/" in out_file:
        os.makedirs(os.path.dirname(out_file), exist_ok=True)

    with open(out_file, "w") as f:
        print(f"% Library: {library.library_id}, Version: {library.last_modified_version()}", file=f)
        print(f"% This file was automatically generated. Do not update manually!", file=f)
        print(f"", file=f)
        bibtexparser.dump(bibtex_database, f)
        logging.info(f"Wrote BibTeX library to {out_file}")


def get_file_version(filename, library_id):
    if os.path.exists(filename):
        with open(filename) as f:
            header = f.readline()
            match = re.search(r"% Library: (.*?), Version: (\d+)", header)
            if match and match[1] == str(library_id):
                return match[2]
    return None


if __name__ == '__main__':
    main()
