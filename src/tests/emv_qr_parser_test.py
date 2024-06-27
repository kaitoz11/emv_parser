from emv_qr import Parser


def test_parser():
    qr_data = "qr data"
    parser = Parser(qr_data)
    assert parser.parse() == "qr dataparsed data"