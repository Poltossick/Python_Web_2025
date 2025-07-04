# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)
import random as rnd  # -> подключение библиотеки, импортировать всю библиотеку

# print(dir(rnd)) # -> список функций для math
"""['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 
 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
 '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', 
 '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', 
 '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 
 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 
 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 
 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'] 
"""
# lst = ['орёл', 'решка']
# print(rnd.choice(lst))
# print(rnd.randint(0, 10))
# print(rnd.randrange(0, 10, 3))
#
# dct = {
#     'a': 'cat',
#     'b': 'dog',
#     'c': 'rabbit',
#     'd': 'rat',
# }
# keys = list(dct.keys())
# key = rnd.choice(keys)
# print(dct[key])
# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# zara = ['\u2680', '\u2681', '\u2682','\u2683','\u2684','\u2685'] # -> ⚃ ⚁
# for i in range(2):
#     print('choice ', rnd.choice(zara), rnd.choice(zara))
#
# for i in range(2):
#     print('sample', rnd.sample(ENGLISH_ABC, k=3))
# rnd.shuffle(ENGLISH_ABC)
# print(ENGLISH_ABC)

# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# lst = ENGLISH_ABC + [range(0, 10)] + ['!', '@', '/', '%']
# rnd.shuffle(lst)
# password = ''.join(str(lst[:8]))
# print(password)


ENGLISH_ABC = list(chr(ch) for ch in range(ord('a'), ord('z') + 1))
abc = list(set(ENGLISH_ABC) ^ set([x.upper() for x in ENGLISH_ABC]))
simbols = list(['!', '@', '/', '%'])
numbers = '1', '2', '3', '4', '5', '6', '7', '8', '9'
N = 8
temp = abc[:N - 3]
temp.append(rnd.choice(simbols))
temp.append(rnd.choice(numbers))
rnd.shuffle(temp)
password = ''.join(temp)
print(password)

rnd.seed()