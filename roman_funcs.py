valores = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',

}


def to_roman(n):
    result = ''

    #millares
    if n >= 1000:
        result = (n//1000) * valores[1000]
        n -= (n // 1000) * 1000

    if n >= 100:
        if n >= 900:
             result += valores[100] + valores[1000]
        elif n >= 500:
            result += valores[500] + ((n // 100)  - 5 )* valores[100]
        elif n == 400:
            result += valores[100] + valores[500]
        else:
            result += (n // 100) * valores[100]
        n -= (n // 100) * 100
    
    if n >= 10:
        if n >= 90:
            result += valores[10] + valores[100]
        elif n >= 50:
            result += valores[50] + ((n//10)-5) * valores[10]
        elif n == 40:
            result += valores[10] + valores[50]
        else:
            result += (n//10) * valores[10]
        n -= (n // 10 ) * 10
    
    if n >= 1:
        if n == 9:
            result += valores[1] + valores[10]
        elif n >= 5:
            result += valores[5] + (n - 5) * valores[1]
        elif n == 4:
            result += valores[1] + valores[5]
        else:
            result += n * valores[1]
        
    return result


