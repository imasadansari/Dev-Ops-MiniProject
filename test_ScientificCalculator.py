"""
Unit tests for the calculator library
"""
# Import the Scientific Calculator Function File

import Scientific_Calculator


class TestCalculator:

    def test_sqrt(self):
        assert Scientific_Calculator.square_root(196) == 14.0
        assert Scientific_Calculator.square_root(0) == 0.0
        assert Scientific_Calculator.square_root(-9) == -9.0
        assert Scientific_Calculator.square_root(1) == 1
        assert Scientific_Calculator.square_root(3) == 1.7320508075688772
        
    def test_factorial(self):
        assert Scientific_Calculator.factorial(7) == 5040
        assert Scientific_Calculator.factorial(5) == 120
        assert Scientific_Calculator.factorial(0) == 1
        assert Scientific_Calculator.factorial(1) == 1
        assert Scientific_Calculator.factorial(-5) == 0.0
        assert Scientific_Calculator.factorial(-5.5) == 0.0
        assert Scientific_Calculator.factorial(5.5) == 6
        
    def test_log(self):
    	assert Scientific_Calculator.natural_log(0) == 0
    	assert Scientific_Calculator.natural_log(-1) == 0
    	assert Scientific_Calculator.natural_log(-10) == 0
    	assert Scientific_Calculator.natural_log(2.718281828459045) == 1.0
    	assert Scientific_Calculator.natural_log(20) == 2.995732273553991
    	
    def test_power(self):
    	assert Scientific_Calculator.power(2,9) == 512
    	assert Scientific_Calculator.power(0, 12) == 0
    	assert Scientific_Calculator.power(20, 0) == 1
    	assert Scientific_Calculator.power(20, 1) == 20.0
    	assert Scientific_Calculator.power(2, 3) == 8.0
    	assert Scientific_Calculator.power(-2,3) == -8.0
    	assert Scientific_Calculator.power(2,-3) == 0.125
    	assert Scientific_Calculator.power(-2, -3) == -0.125
    	assert Scientific_Calculator.power(-2, 4) == 16.0
    	assert Scientific_Calculator.power(1, 23) == 1.0

