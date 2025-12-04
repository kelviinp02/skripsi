#!/usr/bin/env python3
"""
Unit tests for Format 3 module.
"""

import unittest
from format3 import Format3, format3_quick


class TestFormat3(unittest.TestCase):
    """Test cases for Format 3 formatter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sample_data = [
            {"Name": "Alice", "Age": 20, "Grade": "A"},
            {"Name": "Bob", "Age": 21, "Grade": "B"},
        ]
    
    def test_basic_formatting(self):
        """Test basic data formatting."""
        formatter = Format3()
        result = formatter.format_data(self.sample_data)
        
        # Check that result is not empty
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
        # Check that delimiter is present
        self.assertIn("|", result)
        
        # Check that data values are present
        self.assertIn("Alice", result)
        self.assertIn("Bob", result)
        self.assertIn("20", result)
        self.assertIn("21", result)
    
    def test_empty_data(self):
        """Test formatting empty data."""
        formatter = Format3()
        result = formatter.format_data([])
        
        self.assertEqual(result, "")
    
    def test_custom_delimiter(self):
        """Test custom delimiter."""
        formatter = Format3(delimiter="::")
        result = formatter.format_data(self.sample_data)
        
        # Check that custom delimiter is used
        self.assertIn("::", result)
        self.assertNotIn("|", result)
    
    def test_no_padding(self):
        """Test formatting without padding."""
        formatter = Format3(padding=False)
        result = formatter.format_data(self.sample_data)
        
        # Result should still contain data
        self.assertIn("Alice", result)
        self.assertIn("Bob", result)
    
    def test_single_item_format(self):
        """Test single item formatting."""
        formatter = Format3()
        item = {"ID": "123", "Status": "Active"}
        result = formatter.format_single(item)
        
        # Check structure
        self.assertIn("ID: 123", result)
        self.assertIn("Status: Active", result)
        self.assertTrue(result.startswith("|"))
        self.assertTrue(result.endswith("|"))
    
    def test_quick_format(self):
        """Test quick format function."""
        result = format3_quick(self.sample_data)
        
        # Should produce same result as basic formatter
        self.assertIsNotNone(result)
        self.assertIn("Alice", result)
        self.assertIn("Bob", result)
    
    def test_quick_format_custom_delimiter(self):
        """Test quick format with custom delimiter."""
        result = format3_quick(self.sample_data, delimiter="||")
        
        self.assertIn("||", result)
    
    def test_different_data_types(self):
        """Test formatting with different data types."""
        data = [
            {"String": "text", "Number": 123, "Float": 45.67},
            {"String": "more", "Number": 456, "Float": 89.01},
        ]
        
        formatter = Format3()
        result = formatter.format_data(data)
        
        # All values should be converted to strings
        self.assertIn("123", result)
        self.assertIn("45.67", result)
        self.assertIn("text", result)
    
    def test_missing_keys(self):
        """Test formatting with missing keys in some items."""
        data = [
            {"Name": "Alice", "Age": 20, "Grade": "A"},
            {"Name": "Bob", "Age": 21},  # Missing Grade
        ]
        
        formatter = Format3()
        result = formatter.format_data(data)
        
        # Should handle missing keys gracefully
        self.assertIn("Alice", result)
        self.assertIn("Bob", result)


if __name__ == "__main__":
    unittest.main()
