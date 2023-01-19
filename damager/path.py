
from __future__ import annotations

from os.path import split as split_path


def generate_path(*,
                  source_path: str,
                  suffix: str = "_temp",
                  file_format: str | None = None
                  ) -> str:
    """ Generate path for temp and output files """

    tmp_path = split_path(source_path)[-1]
    return ".".join(
        [
            ".".join(tmp_path.split(".")[:-1]) + suffix,
            file_format or tmp_path.split(".")[-1]
         ]
    )

