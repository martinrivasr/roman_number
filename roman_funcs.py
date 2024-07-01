def to_roman(valor):
    result = ""
    if valor == 1:
        result = "I"
    elif valor == 5:
        result ="V"
    elif valor == 10:
        result = "X"
    elif valor == 50:
        result = "L"
    elif valor == 100:
        result = "C"
    elif valor == 500:
        result = "D"
    elif valor == 1000:
        result = "M"
    return result