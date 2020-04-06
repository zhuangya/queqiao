from os import getcwd
from pathlib import Path
from typing import List, Tuple

from pypinyin import Style, slug


def parse_luna_dict(luna_dict_file: Path) -> Tuple[str, List[str]]:
    with open(luna_dict_file) as stream:
        meta, dict = stream.read().split("...")
        meta = meta.replace("luna", "terra")

        luna_dict = list(filter(lambda x: len(x) > 0, dict.splitlines()))

        return (meta, luna_dict)


def transform_line(line: str) -> str:
    word = line.split("\t")[0]
    return "\t".join([word, slug(word, style=Style.TONE3, separator="")])


def get_terra_content(luna_dict_file_path: Path) -> str:
    meta, luna_dict = parse_luna_dict(Path(luna_dict_file_path))

    dict = "\n".join(map(lambda x: transform_line(x), luna_dict))

    return meta + "...\n\n" + dict


def write_terra_file(
    luna_dict_file_path: Path, content: str
) -> None:  # pragma: no cover
    dest = Path(getcwd()) / Path(str(luna_dict_file_path).replace("luna", "terra")).name

    with open(dest, "w") as f:
        f.write(content)


def process(filepath: Path):  # pragma: no cover
    write_terra_file(filepath, get_terra_content(filepath))
