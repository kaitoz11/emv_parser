class Parser:
    def __init__(self, qr_data):
        self.qr_data = qr_data

    def parse(self) -> str:
        """
        Parse the QR data and return the parsed data
        """
        return self.qr_data+"parsed data"
    

class Tag:
    def __init__(self, tag: str, value: str):
        self.tag = tag
        self.value = value

    def __str__(self):
        return f"{self.tag}{len(self.value):02}{self.value}"

    def __repr__(self):
        return f"{self.tag}{len(self.value):02}{self.value}"
    

def encode_tag(value: list[Tag]) -> str:
    result = ""
    for tag in value:
        result += str(tag)

    return result

def decode_tag(value: str) -> list[Tag]:
    pass