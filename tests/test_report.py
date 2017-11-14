import pytest

from pytest_json.report import JSONReport


def test_inline_plugin(testdir):
    """Test json results output."""
    test_file = testdir.makepyfile("""
        def test_foo():
            assert 1 == 1
    """)

    plugin = JSONReport()
    result = pytest.main([test_file.strpath], plugins=[plugin])

    assert result == 0
    assert plugin.json_report['report']['summary']['passed'] == 1
