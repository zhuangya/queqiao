from os import getcwd
from pathlib import Path
from typing import List, Tuple

from pypinyin import Style, lazy_pinyin


def spell_terra(word: str) -> str:
    return "".join(lazy_pinyin(word, style=Style.TONE3))


def parse_luna_dict(luna_dict_file: Path) -> Tuple[str, List[str]]:
    with open(luna_dict_file) as stream:
        file_content = stream.read()

        content = file_content.split("...")

        meta = content[0].replace("luna", "terra")
        dict = content[1]

        luna_dict = [word for word in dict.splitlines() if len(word) > 0]

        return (meta, luna_dict)


def transform_line(line: str) -> str:
    words = line.split("\t")
    return "\t".join([words[0], spell_terra(words[0])])


def process_luna_dict(luna_dict: List[str]) -> List[str]:
    return [transform_line(line) for line in luna_dict]


def get_terra_content(luna_dict_file_path: Path) -> str:
    content = parse_luna_dict(Path(luna_dict_file_path))

    meta = content[0]
    dict = process_luna_dict(content[1])

    return meta + "...\n\n" + "\n".join(dict)


def write_terra_file(luna_dict_file_path: Path, content: str) -> None:
    dest = Path(getcwd()) / Path(luna_dict_file_path).name

    with open(dest, "w") as f:
        f.write(content)


def process(filepath: Path):
    write_terra_file(filepath, get_terra_content(filepath))
