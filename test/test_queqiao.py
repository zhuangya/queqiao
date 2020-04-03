import tempfile
from os import chdir, path

from queqiao.queqiao import (
    get_dest_filename,
    parse_luna_dict,
    process_luna_dict,
    spell_terra,
)


def test_spell_terra() -> None:
    assert spell_terra("中心") == "zhong1xin1"


def test_parse_luna_dict() -> None:
    assert parse_luna_dict("./test/example.dict.yaml") == [
        "阿宝\ta bao",
        "阿爆\ta bao",
        "阿本\ta ben",
        "阿才\ta cai",
        "阿德里安布劳迪\ta de li an bu lao di",
        "阿弟\ta di",
        "阿弟仔\ta di zai",
        "阿杜\ta du",
        "阿朵\ta duo",
    ]


def test_process_luna_dict() -> None:
    assert process_luna_dict(["你好\tni hao", "再见\tzai jian"]) == [
        "你好\tni3hao3",
        "再见\tzai4jian4",
    ]


def test_get_dest_filename() -> None:
    temp_dir = tempfile.TemporaryDirectory()
    chdir(temp_dir.name)

    assert (
        get_dest_filename("luna_pinyin.example.dict.yaml")
        == path.realpath(temp_dir.name) + "/terra_pinyin.example.dict.yaml"
    )

    temp_dir.cleanup()
