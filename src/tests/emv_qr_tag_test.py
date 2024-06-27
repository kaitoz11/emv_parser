from emv_qr import Tag, encode_tag

def test_tag():
    tag = Tag("00", "value")
    assert str(tag) == "0005value"
    assert repr(tag) == "0005value"
    assert tag.tag == "00"
    assert tag.value == "value"

def test_generator():
    qr = [
        Tag("00", "01"),
        Tag("01", "wthub"),
        Tag("05", "xin chào tất cả mọi người"),
        Tag("07", "https://wthub.com"),
        Tag("99", encode_tag([
            Tag("00", "hehe"),
        ]))
    ]
    assert encode_tag(qr) == "0002010105wthub0525xin chào tất cả mọi người0717https://wthub.com99080004hehe"