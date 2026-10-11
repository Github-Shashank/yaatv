import pytest

from yaatv.models import _float_or_none


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("123.5", 123.5),
        (None, None),
        ("invalid", None),
        ("nan", None),
        ("inf", None),
        ("-inf", None),
    ],
)
def test_float_or_none_normalizes_invalid_values(
    value: object, expected: float | None
) -> None:
    assert _float_or_none(value) == expected
