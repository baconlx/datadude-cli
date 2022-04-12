
import pathlib

def clean_pattern(p):
    if isinstance(p, Pattern):
        return p
    elif isinstance(p, list):
        return [item for sublist in p for item in clean_pattern(sublist)]
    elif isinstance(p, dict):
        return [item for sublist in p.values() for item in clean_pattern(sublist)]
    elif isinstance(p, tuple):
        return [item for sublist in list(p) for item in clean_pattern(sublist)]
    elif isinstance(p, bytes):
        return list(p)
    elif isinstance(p, bool):
        return [int(p)]
    elif isinstance(p, int):
        return [p]
    elif isinstance(p, str):
        try:
            return get_valid_byte_from_byte_string(p)
        except Exception as e:
            raise Exception("invalid item in pattern string: " + str(p))
    else:
        raise Exception("invalid item in pattern: " + str(p))

def get_valid_byte_from_byte_string(v):
    value = v.strip().lower()
    if value == "*" or value == "?":
        return [value]
    else:
        try:
            hexbytes = value.replace('0x', '').replace(' ', '')
            # TODO: hexbytes are wrong if string length is odd (0xAA01 != 0xAA1)
            return [int(item, 16) for item in [hexbytes[i:i+2] for i in range(0, len(hexbytes), 2)]]
        except Exception:
            raise Exception("pattern value is not valid: " + str(value))

class Pattern():
    def __init__(self, data = None):
        self.orig_data = data
        self.pattern = clean_pattern(data)

    def __str__(self):
        return str(self.pattern)

    def get(self):
        return self.pattern

class DataResource():
    def __init__(self):
        self.resource = None

    def __str__(self):
        return str(self.resource) if not self.resource == None else str("<UNDEFINED RESOURCE>")

    def is_valid(self):
        if self.resource == None:
           raise Exception("resource not valid")

class FileResource(DataResource):
    def __init__(self, resource = None):
        super().__init__()
        self.resource = resource
        
        if not resource == None:
            self.set(resource)

    def set(self, value):
        if isinstance(value, pathlib.Path):
            self.resource = value
        if isinstance(value, str):
            self.resource = pathlib.Path(value).absolute()

        self.is_valid()

    def is_valid(self):
        super().is_valid()
        if not self.resource.exists():
            raise Exception("file does not exist: " + str(self.resource))
        if not self.resource.is_file():
            raise Exception("resource is not a file: " + str(self.resource))


    def search_pattern(self, _pattern = None):
        pattern = None

        if isinstance(_pattern, list):
            pattern = Pattern(_pattern)
        elif isinstance(_pattern, Pattern):
            pattern = _pattern
        else:
            raise Exception("no valid pattern for searching: " + str(_pattern))

        # print("searching ...")
        # print(pattern)
        # print("in " + str(self.resource))

        # if not isinstance(pattern, Pattern):
        #     raise Exception("no valid datadude pattern")



    




