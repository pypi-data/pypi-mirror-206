"""Console script for RibosomeProfiler."""
import argparse
import sys

from RibosomeProfiler import argumnet_parser, main


def cli_main():
    """Console script for RibosomeProfiler."""
    parser = argumnet_parser()
    args = parser.parse_args()

    main(args)
    return 0


if __name__ == "__main__":
    sys.exit(cli_main())  # pragma: no cover
