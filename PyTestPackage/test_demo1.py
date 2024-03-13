import pytest

def test_m1():
    a=3
    b=4
    assert a+1==b,"test passed"
    assert a!=b,"test pass as a=b"


def test_m2():
    name="Selenium"
    assert name.upper()=="SELENIUM"

def test_m3():
    assert True;

def test_m4():
    assert False;

def test_m5():
    assert "sai"=="SAI", "Test fails because sai is not equal to SAI"

def test_m6():
    i=32
    c=32
    assert id(i)==id(c), "Check for variables"

def test_login1():
    assert "admin"=="admin", "Check for login"
