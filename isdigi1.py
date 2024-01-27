def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

print(is_number(1))
print(is_number(1.0))
print(is_number(0))
print(is_number(-2))
print(is_number(-2.0))
print(is_number("abc"))

