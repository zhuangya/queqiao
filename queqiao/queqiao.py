from typing import List

from pypinyin import Style, lazy_pinyin


def spell_terra(word: str) -> str:
    return "".join(lazy_pinyin(word, style=Style.TONE3))


def parse_luna_dict(luna_dict_file: str) -> List[str]:
    with open(luna_dict_file) as stream:
        file_content = stream.read()

        dict = file_content.split("...")[1]
        luna_dict = [word for word in dict.splitlines() if len(word) > 0]

        return luna_dict


def transform_line(line: str) -> str:
    words = line.split("\t")
    return "\t".join([words[0], spell_terra(words[0])])


def process_luna_dict(luna_dict: List[str]) -> List[str]:
    return [transform_line(line) for line in luna_dict]
