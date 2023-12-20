from two import pair

def test_pair_true():
    assert pair(4) == True;

def test_pair_false():
    assert pair(5) == False;

def test_pair_zero():
    assert pair(0) == True;
