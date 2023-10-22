import unittest
from app import validate_address_pin

class TestAddressValidation(unittest.TestCase):
    def test_valid_address_correct_pin(self):
        address = '2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050'
        result = validate_address_pin("560050", address)
        self.assertTrue(result)

    def test_valid_address_incorrect_pin(self):
        address = '2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095'
        result = validate_address_pin("560050", address)
        self.assertFalse(result)

    def test_valid_address_no_pin(self):
        address = '2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka'
        result = validate_address_pin("", address)
        self.assertTrue(result)

    def test_invalid_address_non_existent(self):
        address = 'Random Address, City, State, 123456'
        result = validate_address_pin("123456", address)
        self.assertFalse(result)

    def test_valid_address_partial_matching_name(self):
        address = 'Ashoknagar, Bangalore South, Bangalore, Karnataka 560050'
        result = validate_address_pin("560050", address)
        self.assertTrue(result)

    def test_valid_address_no_address_details(self):
        address = 'No Address Details, City, State, 123456'
        result = validate_address_pin("123456", address)
        self.assertFalse(result)

    def test_empty_input(self):
        address = ''
        result = validate_address_pin("", address)
        self.assertFalse(result)

    def test_no_6_digit_number_in_address(self):
        address = '2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka'
        result = validate_address_pin("560050", address)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
