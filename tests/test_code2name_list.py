from src.jp_prefectures_simple import code2name


def test_code_int():
    assert code2name([12, 34]) == ["千葉県", "広島県"]
    assert code2name([1, 2, 3]) == ["北海道", "青森県", "岩手県"]
    assert code2name([45, 13, 47]) == ["宮崎県", "東京都", "沖縄県"]
