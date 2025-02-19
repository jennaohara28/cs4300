def get_int():
    return 10

def get_float():
    return 3.14

def get_str():
    return "This is a test"

def get_bool():
    return True

def test_int():
    assert isinstance(get_int(), int)
    assert get_int() == 10

def test_float():
    assert isinstance(get_float(), float) 
    assert get_float() == 3.14 

def test_str():
    assert isinstance(get_str(), str)
    assert get_str() == "This is a test"

def test_bool():
    assert isinstance(get_bool(), bool)
    assert get_bool() is True 
