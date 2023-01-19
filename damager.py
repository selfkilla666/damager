from __future__ import annotations

from argparse import ArgumentParser, FileType

from damager.compress import compress_image
from damager.compress import COMPRESS_FORMATS, OUTPUT_FORMATS

parser = ArgumentParser(
    prog="Damager",
    description="Utility for adding JPEG and WEBP compression artifacts")

parser.add_argument("filename",
                    action="store",
                    default=None,
                    help="Path to image whats need to compress"
                   )

parser.add_argument("compress_format",
                    action="store",
                    default=None,
                    choices=COMPRESS_FORMATS,
                    metavar="compress_format [{}]".format(", ".join(COMPRESS_FORMATS)),
                    help="Compress formats for image")

parser.add_argument("quality",
                    action="store",
                    default=None,
                    choices=range(1, 101),
                    metavar="quality [1-100]",
                    help="Output file quality (in range from 1 to 100)",
                    type=int)

parser.add_argument("-o",
                    "--output",
                    action="store",
                    dest="output_path",
                    default=None,
                    help="Output path to save result"
                   )

parser.add_argument("-f",
                    "--output-format",
                    action="store",
                    dest="output_format",
                    choices=OUTPUT_FORMATS,
                    default="png",
                    metavar="[{}]".format(", ".join(OUTPUT_FORMATS)),
                    help="Output file format")

args = parser.parse_args()

if args:

    file = compress_image(
        source_path=args.filename,
        output_path=args.output_path,
        compress_format=args.compress_format,
        output_format=args.output_format,
        quality=args.quality
    )
    print(f"Damager: image {args.filename} converted to {file}")
