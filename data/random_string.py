import random
import datetime
import string

# random.randint(0, 100)
# random.randrange(10, 100, 2)


# for i in range(0, 100):
# #     print(i, random.randint(0, 100))

t = datetime.datetime.now()
print(t)
print(t.timestamp())
print(t.isoformat())

screenshot_name = "name"+t.isoformat()+".jpeg"
print(screenshot_name)

a = random.choice('assdfhgfhgfhghfghdfwerewqw')
print(a)


b = random.choice([1, 6, 8, 9, 3, 56])
print(b)


c = random.choices("dfdfrewrwerW", k=5)
x =''.join(c)
print(c)
print(x)

print(string.ascii_letters, string.printable)
print("aaaaaaaa")


def random_string1(minlen=1, maxlen=255):
    length = random.randint(minlen, maxlen)
    symbols = (string.ascii_letters + string.digits + string.punctuation + " " * 5)
    print(symbols)
    result = "".join(random.choices(symbols, k=length))
    return result


x = random_string1()
print("randm str: ", x)


def random_string2(minlen=1, maxlen=256, spaces=False, whitespases=False, enter=False, cyr=False):
    length = random.randint(minlen, maxlen)
    symbols = string.ascii_letters + string.digits + string.punctuation
    if spaces:
        symbols += ' ' * 10
    if whitespases:
        symbols += string.whitespace[:-2] * 3
    if enter:
        symbols += "\n"*3
    if cyr:
        cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF)
                              if chr(l).isprintable()])
        symbols += cyr_symbol
    result = ''.join(random.choices(symbols, k=length))
    return result
