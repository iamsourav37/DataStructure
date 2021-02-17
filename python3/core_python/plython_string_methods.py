

if __name__ == '__main__':

    msg = 'hello world. my name is sourav ganguly. i am a futter developer and python developer also.'

    print(msg.capitalize())
    print(msg.count('2'))
    print(msg.casefold())

    print(msg.center(10))
    print(msg.endswith('also.'))
    print(msg.find('world'))
    print(msg.find('world_hello'))
    print(msg.index('is'))
    # print(msg.index('is_is')) # ERROR this line

    print(msg.isalnum())  # return false because this string does not have any number , it is not a alpha numeric only alpha

    print(msg.isalpha())  # false beacause space is not alphabet

    print(msg.isdigit())
    print("37".isdigit())

    print("check upper".isupper())
    print("is lower".islower())

    a = 'hello'
    b = ''
    b = b.join(a)
    print(b)

    mytuple = ('aplle', 'banana', 'mango')
    x = ' '.join(mytuple)
    y = '<->'.join(mytuple)
    print(x)
    print(y)

    d1 = {
        'key1': 'value',
        'key2': 'value2'
    }

    z = '#'.join(d1)
    print(z)

    s1 = '  hello  world  I am a Python Developer         '
    print(s1)
    print(s1.strip())

    txt = "^^^^,,,,....banana....rrr"

    x = txt.strip("^,.r")
    print(x)