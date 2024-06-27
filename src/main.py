from emv_qr import Tag, encode_tag, decode_tag

qr = [
    Tag("00", "00"),
    Tag("01", "01"),
    Tag("05", "hello world"),
]