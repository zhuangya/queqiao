from queqiao.queqiao import fib, parse_luna_dict, process_luna_dict, spell_terra


def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55


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
