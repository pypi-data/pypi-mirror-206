import pytest
from datetime import datetime, time
from frictionless import FrictionlessException, Dialect, formats
from frictionless.resources import TableResource


# Read


def test_sql_parser(database_url):
    control = formats.SqlControl(table="table")
    with TableResource(path=database_url, control=control) as resource:
        assert resource.schema.to_descriptor() == {
            "fields": [
                {"name": "id", "type": "integer"},
                {"name": "name", "type": "string"},
            ],
            "primaryKey": ["id"],
        }
        assert resource.header == ["id", "name"]
        assert resource.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


def test_sql_parser_order_by(database_url):
    control = formats.SqlControl(table="table", order_by="id")
    with TableResource(path=database_url, control=control) as resource:
        assert resource.header == ["id", "name"]
        assert resource.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


def test_sql_parser_order_by_desc(database_url):
    control = formats.SqlControl(table="table", order_by="id desc")
    with TableResource(path=database_url, control=control) as resource:
        assert resource.header == ["id", "name"]
        assert resource.read_rows() == [
            {"id": 2, "name": "中国人"},
            {"id": 1, "name": "english"},
        ]


def test_sql_parser_where(database_url):
    control = formats.SqlControl(table="table", where="name = '中国人'")
    with TableResource(path=database_url, control=control) as resource:
        assert resource.header == ["id", "name"]
        assert resource.read_rows() == [
            {"id": 2, "name": "中国人"},
        ]


def test_sql_parser_table_is_required_error(database_url):
    resource = TableResource(path=database_url)
    with pytest.raises(FrictionlessException) as excinfo:
        resource.open()
    error = excinfo.value.error
    assert error.type == "error"
    assert error.note.count('Please provide "dialect.sql.table" for reading')


# The output is quite weird but it's a correct output for SQL with header=False
def test_sql_parser_header_false(database_url):
    control = formats.SqlControl(table="table")
    dialect = Dialect(header=False, controls=[control])
    with TableResource(path=database_url, dialect=dialect) as resource:
        assert resource.header.missing
        assert resource.read_rows() == [
            {"id": None, "name": "name"},
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


# Write


def test_sql_parser_write(database_url):
    source = TableResource(path="data/table.csv")
    control = formats.SqlControl(table="name", order_by="id")
    target = source.write(path=database_url, control=control)
    with target:
        assert target.header == ["id", "name"]
        assert target.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


def test_sql_parser_write_where(database_url):
    source = TableResource(path="data/table.csv")
    control = formats.SqlControl(table="name", where="name = '中国人'")
    target = source.write(path=database_url, control=control)
    with target:
        assert target.header == ["id", "name"]
        assert target.read_rows() == [
            {"id": 2, "name": "中国人"},
        ]


def test_sql_parser_write_timezone(sqlite_url):
    source = TableResource(path="data/timezone.csv")
    control = formats.SqlControl(table="timezone")
    target = source.write(path=sqlite_url, control=control)
    with target:
        assert target.header == ["datetime", "time"]
        assert target.read_rows() == [
            {
                "datetime": datetime(2020, 1, 1, 15),
                "time": time(15),
            },
            {
                "datetime": datetime(2020, 1, 1, 15),
                "time": time(15),
            },
            {
                "datetime": datetime(2020, 1, 1, 12),
                "time": time(12),
            },
            {
                "datetime": datetime(2020, 1, 1, 18),
                "time": time(18),
            },
        ]


# Bugs


def test_sql_parser_write_string_pk_issue_777_sqlite(sqlite_url):
    source = TableResource(path="data/table.csv")
    source.infer()
    source.schema.primary_key = ["name"]
    control = formats.SqlControl(table="name")
    target = source.write(path=sqlite_url, control=control)
    with target:
        assert target.schema.primary_key == ["name"]
        assert target.header == ["id", "name"]
        assert target.read_rows() == [
            {"id": 1, "name": "english"},
            {"id": 2, "name": "中国人"},
        ]


def test_sql_parser_describe_to_yaml_failing_issue_821(database_url):
    control = formats.SqlControl(table="table")
    resource = TableResource(path=database_url, control=control)
    resource.infer()
    assert resource.to_yaml()
