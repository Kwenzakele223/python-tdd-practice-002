import unittest
from main import *


class TestFibonacci(unittest.TestCase):
    
    def test_small_nth(self):
        self.assertEqual(fibonacci(1),[0])
        self.assertEqual(fibonacci(2),[0,1])
        self.assertEqual(fibonacci(5),[0,1,1,2,3])
        self.assertEqual(fibonacci(8),[0,1,1,2,3,5,8,13])
        
    def test_large_nth(self):
        self.assertEqual(fibonacci(12),[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(fibonacci(18),[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597])
        self.assertEqual(fibonacci(20),[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])
        
    def test_edge(self):
        self.assertEqual(fibonacci(0),[])
        self.assertEqual(fibonacci(-1),[])
        
        
class TestEven(unittest.TestCase):
    
    def test_even_numbers_len(self):
        self.assertEqual(len(even([2,1,9,4,8,16,16])),5)
        self.assertEqual(len(even([1,9,4,8,16])),3)
        
    def test_even_ascending_order(self):
        self.assertEqual(even([2,1,9,4,8,16]),[2,4,8,16])
        self.assertEqual(even([16,9,4,8,12,4]),[4,4,8,12,16])

class TestOdd(unittest.TestCase):
    
    def test_odd_numbers_len(self):
        self.assertEqual(len(odd([2,1,9,4,8,16])),2)
        self.assertEqual(len(odd([9,4,8,16])),1)
        
    def test_odd_descending_order(self):
        self.assertEqual(odd([2,1,9,4,8,16]),[9,1])
        self.assertEqual(odd([5,16,3,9,4,8,12]),[9,5,3])
        self.assertEqual(odd([5,16,3,9,4,8,12]),[9,5,3])
        self.assertEqual(odd([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),[21,13,5,3,1,1])

class TestEvenVsOdd(unittest.TestCase):
    
    def test_even_vs_odd(self):
        self.assertEqual(even_vs_odd([1,2,3,8,5]),'Even')
        self.assertEqual(even_vs_odd([0,2,3,8,5]),'Even')
        self.assertEqual(even_vs_odd([1,2,3,4,5,6,19]),'Odd')
        
    def test_even_vs_odd_tie_and_edge(self):
        self.assertEqual(even_vs_odd([]),'Tie')
        self.assertEqual(even_vs_odd([0,1,4,3,10,9,1]),'Tie')
        self.assertEqual(even_vs_odd([0,0]),'Tie')
        
class TestIsPrime(unittest.TestCase):
    
    def test_is_prime_false(self):
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(20))
        
    def test_is_prime_true(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(17))
        
    def test_is_prime_edge_and_exception(self):
        self.assertFalse(is_prime(0))
        
        with self.assertRaises(ValueError):
            is_prime(-1)
        with self.assertRaises(ValueError):
            is_prime([])
        with self.assertRaises(ValueError):
            is_prime("7")
        with self.assertRaises(ValueError):
            is_prime({'n':7})
            
class TestGenerateEmail(unittest.TestCase):
    
    
    def test_generate_email(self):
        self.assertEqual(generate_email('Auston Mtabane','2024','jhb'),     'aumtajhb024@student.wethinkcode.co.za')
        self.assertEqual(generate_email('Neo Phukubye','2025','jhb'),       'nephujhb025@student.wethinkcode.co.za')
        self.assertEqual(generate_email('Kwenzakele	Shongwe','2025','jhb'), 'kwshojhb025@student.wethinkcode.co.za')
        self.assertEqual(generate_email('Khatisani Mongwe','2025','jhb'),   'khmonjhb025@student.wethinkcode.co.za')
        self.assertEqual(generate_email('Agnes Chauke','2025','jhb'),       'agchajhb025@student.wethinkcode.co.za')
        self.assertEqual(generate_email("Karabo	Mahlare",'2025','jhb'),     'kamahjhb025@student.wethinkcode.co.za')

    def test_generate_email_edge(self):
        self.assertEqual(generate_email('Oriel Kopano Dibakoane','2027','cpt'),      'ordibcpt027@student.wethinkcode.co.za')
        self.assertEqual(generate_email('Nkosingiphile Lindani Sukati','2025','jhb'),'nksukjhb025@student.wethinkcode.co.za')


            
if __name__ == '__main__':
    unittest.main()
        
        
            
