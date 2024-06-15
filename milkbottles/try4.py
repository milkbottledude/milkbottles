def insertColumn(num_of_cols):
    print(str(int(num_of_cols) * 'a'))

def sayhi():
    return 'hi'

def standard_form(messyshi):
    messy = float('%.3g' % messyshi)
    if messy > 1000000000:
        return f'{messy/1000000000}b'
    elif messy > 1000000:
        return f'{messy/1000000}m'
    elif messy > 1000:
        return f'{messy/1000}k'
    
standard_form(1234567)