import pytest
from jar import Jar


def test_init():
    """Test jar initialization with different capacities"""
    jar = Jar()
    assert jar.capacity == 12
    
    jar = Jar(5)
    assert jar.capacity == 5
    
    with pytest.raises(ValueError):
        Jar(-1)
    
    with pytest.raises(ValueError):
        Jar("10")


def test_str():
    """Test string representation of jar"""
    jar = Jar()
    assert str(jar) == ""
    
    jar.deposit(1)
    assert str(jar) == "🍪"
    
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    """Test depositing cookies into jar"""
    jar = Jar()
    
    jar.deposit(5)
    assert jar.size == 5
    
    jar.deposit(3)
    assert jar.size == 8
    
    with pytest.raises(ValueError):
        jar.deposit(10)
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    """Test withdrawing cookies from jar"""
    jar = Jar(10)
    jar.deposit(8)
    
    jar.withdraw(3)
    assert jar.size == 5
    
    jar.withdraw(2)
    assert jar.size == 3
    
    with pytest.raises(ValueError):
        jar.withdraw(5)

    with pytest.raises(ValueError):
        jar.withdraw(-1)
