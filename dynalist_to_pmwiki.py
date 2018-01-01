import re
import math
import sys

def fix_italics(line):
    return re.sub("__", "''", line)

def fix_bold(line):
    return re.sub("\*\*", "'''", line)

def _find_indentation(line):
    indentation_match = re.match(" *", line)
    matched_substring = indentation_match.group(0)
    return int(math.floor(len(matched_substring) / 4)) - 1
    
def fix_indentation(line):
    indent_count = _find_indentation(line)
    pmwiki_indent_string = "*" * indent_count
    return re.sub("^ *", pmwiki_indent_string, line)

def convert_dynalist_pmwiki(dynalist_file, pmwiki_file):
    for line in dynalist_file:
        output_line = fix_indentation(fix_bold(fix_italics(line)))
        pmwiki_file.write(output_line)

def print_usage():
    print("Usage: python dynalist_to_pmwiki.py dynalist_file pmwiki_file")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(-1)
    with open(sys.argv[1], 'r') as dynalist_file:
        with open(sys.argv[2], 'w') as pmwiki_file:
            convert_dynalist_pmwiki(dynalist_file, pmwiki_file)

    
