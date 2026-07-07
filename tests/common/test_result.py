from mfm.common.result import Result


def test_ok_result():
    result = Result.ok(42)

    assert result.success
    assert result.value == 42


def test_fail_result():
    result = Result.fail("Error")

    assert not result.success
    assert result.message == "Error"