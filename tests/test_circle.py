import pytest
import source.shapes as shapes
import math


class Testcircle:
    
    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shapes.circle(10)
        
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle
    
    def test_area(self): 
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        
    def test_parameter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
    