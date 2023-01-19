
from __future__ import annotations

from typing import Literal, List
from PIL import Image
from os import remove as remove_file

from .path import generate_path


COMPRESS_FORMATS: List[str] = ["jpeg", "webp"]
OUTPUT_FORMATS: List[str] = ["jpeg", "webp", "png"]


def compress_image(*,
                   source_path: str,
                   output_path: str = None,
                   compress_format: Literal["jpeg", "webp"],
                   output_format: Literal["jpeg", "webp", "png"] = "png",
                   quality: int
                   ) -> str:
    """ Compress image and save output to file """

    # Create temp image file with compression
    temp_file_path = generate_path(
        source_path=source_path,
        file_format=compress_format
    )
    temp_image = Image.open(source_path).convert("RGB")
    temp_image.save(
        temp_file_path,
        compress_format,
        optimize=True,
        quality=quality
    )

    # Save compressed file
    output_image = Image.open(temp_file_path).convert("RGB")
    output_path = output_path or generate_path(
            source_path=source_path,
            suffix=f"_output_{compress_format}_with_{quality}_quality",
            file_format=output_format)
    output_image.save(
        output_path,
        output_format
    )

    # Clear temp file for compress
    remove_file(temp_file_path)

    return output_path