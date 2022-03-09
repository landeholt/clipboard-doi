import argparse
from functools import reduce
from bibcure import get_bib_from_doi
from pyperclip import copy
import re

def build_bib(bibs, doi):

    found, bib = get_bib_from_doi(doi)
    if found:
        return [*bibs, bib]

def join_bib(bib_gen, delimiter='\n\n'):
    return delimiter.join(bib_gen)

def url_decode(bib_string):
    return re.sub(r"%2F", "/", bib_string)
    
def doi2cb():
    parser = argparse.ArgumentParser(
        prog="doi2cb"
    )

    args = parser.parse_known_args()

    dois = args[1]
    inlinedoi = len(dois) > 0

    if inlinedoi:

        
        bib_generator = reduce(build_bib, dois, [])
        if bib_generator:
            bib_string = url_decode(join_bib(bib_generator))
            copy(bib_string)
            print("bib saved to clipboard")
            return
    
    print("no bibs found")
