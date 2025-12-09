import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from calc import add, sub, mult, div, log, square, sin, cos, sqrt, perc

#Add Tests
def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10
#--------------------------

#Sub Tests
def test_sub():
    assert sub(6, 5) == 1

def test_sub2():
    assert sub(5, 6) == -1

def test_sub3():
    assert sub(15, 20) != 5
#--------------------------

#Mult Tests
def test_mult():
    assert mult(2, 5) == 10

def test_mult2():
    assert mult(5, 3) != 8

def test_mult3():
    assert mult(-2, 5) == -10

def test_mult4():
    assert mult(5, 0) == 0
#----------------------------

#Div Tests
def test_div():
    assert div(15, 3) == 5

def test_div2():
    assert div(-25, 5) == -5

def test_div3():
    assert div(1, 5) == 0.20

def test_div4():
    assert div(-2, 0) == "N/A"

def test_div5():
    assert div(0, 6) != "N/A" 
#----------------------------

#Log Tests
def test_log():
    assert log(10) == 1

def test_log2():
    assert log(8, 2) == 3

def test_log3():
    assert log(10, 2) != 1
#--------------------------

#Square Tests
def test_square():
    assert square(8) == 64

def test_square2():
    assert square(3) != 6
#-------------------------

#Sin Tests
def test_sin():
    assert sin(1.5708) == 1

def test_sin2():
    assert sin(0) == 0
#--------------------------

#Cos Tests
def test_cos():
    assert cos(1.5708) == 0

def test_cos2():
    assert cos(0) == 1
#--------------------------

#Sqrt Tests
def test_sqrt():
    assert sqrt(49) == 7

def test_sqrt2():
    assert sqrt(0) == 0

def test_sqrt3():
    assert sqrt(-9) != 3

def test_sqrt4():
    assert sqrt(-1) == "N/A"

def test_sqrt5():
    assert sqrt(1) != 2
#--------------------------

#Perc Tests
def test_perc():
    assert perc(0.1) == "10%"

def test_perc2():
    assert perc(0.5) != 50

def test_perc3():
    assert perc(50) == "5000%"
