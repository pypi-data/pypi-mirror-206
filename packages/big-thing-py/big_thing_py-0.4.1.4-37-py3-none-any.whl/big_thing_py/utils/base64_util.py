import base64


def file_to_base64(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()


def base64_to_file(base64_string: str, file_path: str) -> None:
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(base64_string))


def string_to_base64(string: str):
    return base64.b64encode(string.encode()).decode()


def base64_to_string(base64_string: str):
    return base64.b64decode(base64_string).decode()


def is_base64(s):
    try:
        base64.b64decode(s)
        return True
    except:
        return False


if __name__ == '__main__':
    print(string_to_base64('100'))
