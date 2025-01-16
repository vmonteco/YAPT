import random
import string

empty_case = {
    'name': 'empty case',
    "cases": [(b'',),]
}
simple_short_string_cases = {
    'name': 'simple short string cases',
    'cases': [
        (b'a',),
        (b'b',),
        (b'foo',),
    ],
}
simple_long_string_cases = {
    'name': 'simple long string cases',
    'cases': [
        (b'c' * 1000,),
        (b'c' * 1024,),
        (b'c' * 2046,),
        (bytes(''.join(random.choice(string.digits) for i in range(1000)), encoding="ascii"),),
        (bytes(''.join(random.choice(string.digits) for i in range(1024)), encoding="ascii"),),
        (bytes(''.join(random.choice(string.digits) for i in range(2048)), encoding="ascii"),),
        (bytes(''.join(random.choice(string.digits) for i in range(2049)), encoding="ascii"),),
    ]
}

simple_cases = [
    empty_case,
    simple_short_string_cases,
    simple_long_string_cases,
]


def cases_generator():
    return simple_cases
