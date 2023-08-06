from frictionless import formats
from frictionless.resources import TableResource


# Read


def test_jsonl_parser():
    with TableResource(path="data/table.jsonl") as resource:
        assert resource.header == ["id", "name"]
        assert resource.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


def test_jsonl_parser_ndjson():
    with TableResource(path="data/table.ndjson") as resource:
        assert resource.header == ["id", "name"]
        assert resource.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


# Write


def test_jsonl_parser_write(tmpdir):
    source = TableResource(path="data/table.csv")
    target = source.write(path=str(tmpdir.join("table.jsonl")))
    with target:
        assert target.header == ["id", "name"]
        assert target.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


def test_jsonl_parser_write_keyed(tmpdir):
    control = formats.JsonControl(keyed=True)
    source = TableResource(path="data/table.csv")
    target = source.write(path=str(tmpdir.join("table.jsonl")), control=control)
    with target:
        assert target.header == ["id", "name"]
        assert target.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]
