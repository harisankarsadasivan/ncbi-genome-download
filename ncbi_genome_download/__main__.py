import os
import argparse

import ncbi_genome_download


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain',
                        choices=['all'] + ncbi_genome_download.available_domains,
                        help='The NCBI "domain" to download')
    parser.add_argument('-o', '--output-folder',
                        dest='output', default=os.getcwd(),
                        help='Create output hierarchy in specified folder (default: current directory)')
    parser.add_argument('-v', '--verbose',
                        action='store_true', default=False,
                        help='increase output verbosity')
    parser.add_argument('-d', '--debug',
                        action='store_true', default=False,
                        help='print debugging information')
    parser.add_argument('-V', '--version',
                        action='version', version=ncbi_genome_download.__version__,
                        help='print version information')

    args = parser.parse_args()

    ncbi_genome_download.download(args)

if __name__ == '__main__':
    main()