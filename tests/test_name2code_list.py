"""Tests for name2code function with list input."""
from src.jp_prefectures_simple import name2code



def test_name():
    """Test converting a list of prefecture names to codes."""

    assert name2code(["東京都", "北海道"]) == ["13", "01"]
    assert name2code(["大阪府", "福岡県", "沖縄県"]) == ["27", "40", "47"]
    assert name2code(["愛知県"]) == ["23"]
    assert name2code(["神奈川県", "千葉県", "埼玉県"]) == ["14", "12", "11"]


if __name__ == "__main__":
    test_name()
