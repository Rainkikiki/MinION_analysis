__author__ = 'flashton'

'''
This section of the code is heavily influenced by the design of Aaron Quinlan and Nick Loman's poretools package - check it out!
https://github.com/arq5x/poretools
'''

import argparse
from __init__ import __version__
import run_last

class ArgumentParserWithDefaults(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(ArgumentParserWithDefaults, self).__init__(*args, **kwargs)
        self.add_argument("-q", "--quiet", help="Do not output warnings to stderr", action="store_true", dest="quiet")


def run_command(args):

    if args.command == 'run_last':
        run_last.run_last(args.reference, args.minion_reads, args.output_dir)

    if args.command == 'parse_last_output':
        pass

def main():
    parser = argparse.ArgumentParser(prog='minion_analysis', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", help="Installed minion_analysis version", action="version",
                        version="%(prog)s " + str(__version__))

    subparsers = parser.add_subparsers(title='[sub-commands]', dest='command', parser_class=ArgumentParserWithDefaults)

    parser_run_last = subparsers.add_parser('run_last', help='Takes MinION reads and maps then to a reference using LAST')
    parser_run_last.add_argument('minion_reads', metavar='MinION reads in fasta format', help='MinION reads in FASTA format')
    parser_run_last.add_argument('reference', metavar='Reference genome (Illumina contigs)', help='Assembly of Illumina data from the same organism as the MinION reads')
    parser_run_last.add_argument('output_dir', metavar='Directory in which output will be stored', help='Where the output of the LAST alignment and subsequent processing will be stored')

    parser_parse_last_output = subparsers.add_parser('parse_last_output', help='Parses LAST output (in BLAST text format produced by maf-convert) to produce a format useful for scaffolding')
    parser_parse_last_output.add_argument('input_dir', metavar='Directory in which output of minion_analysis run_last was written to', help='Where the output of the LAST alignment and subsequent processing was written to')

    args = parser.parse_args()


if __name__ == "__main__":
    main()