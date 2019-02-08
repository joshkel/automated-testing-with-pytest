def test_math():
    a = 1
    b = 2
    assert a + b == 4


def test_employee():
    actual   = {'first_name': 'John', 'last_name': 'Doe',
                'city': 'Nashville', 'state': 'TN'}

    expected = {'first_name': 'John', 'last_name': 'Doe',
                'city': 'Memphis', 'state': 'TN'}

    assert actual == expected
