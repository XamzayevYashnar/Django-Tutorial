class FourDigitYearConvertor: 
    regex = r"[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%4d" % value

class NameConvertor:

    regex = r"[a-zA-Z0-9_-]+"

    def to_python(self, value):
        return str(value)