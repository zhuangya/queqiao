from pathlib import Path

from queqiao.queqiao import (
    get_terra_content,
    parse_luna_dict,
    process_luna_dict,
    spell_terra,
)


def test_spell_terra() -> None:
    assert spell_terra("中心") == "zhong1xin1"


def test_parse_luna_dict() -> None:
    assert parse_luna_dict(Path("./test/example.dict.yaml")) == (
        """---
name: terra_pinyin.mingxing
version: "2016.06.30"
sort: by_weight
use_preset_vocabulary: false
""",
        [
            "阿宝\ta bao",
            "阿爆\ta bao",
            "阿本\ta ben",
            "阿才\ta cai",
            "阿德里安布劳迪\ta de li an bu lao di",
            "阿弟\ta di",
            "阿弟仔\ta di zai",
            "阿杜\ta du",
            "阿朵\ta duo",
        ],
    )


def test_process_luna_dict() -> None:
    assert process_luna_dict(["你好\tni hao", "再见\tzai jian"]) == [
        "你好\tni3hao3",
        "再见\tzai4jian4",
    ]


def test_get_terra_content() -> None:
    assert (
        get_terra_content(Path("./test/example.dict.yaml"))
        == """---
name: terra_pinyin.mingxing
version: "2016.06.30"
sort: by_weight
use_preset_vocabulary: false
...

阿宝	a1bao3
阿爆	a1bao4
阿本	a1ben3
阿才	a1cai2
阿德里安布劳迪	a1de2li3an1bu4lao2di2
阿弟	a1di4
阿弟仔	a1di4zai3
阿杜	a1du4
阿朵	a1duo3"""
    )
