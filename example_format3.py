#!/usr/bin/env python3
"""
Example usage of Format 3 module.
Demonstrates various formatting capabilities.
"""

from format3 import Format3, format3_quick


def main():
    print("=" * 60)
    print("Format 3 - Example Usage")
    print("=" * 60)
    print()
    
    # Example 1: Basic data formatting
    print("Example 1: Basic Student Data")
    print("-" * 60)
    
    student_data = [
        {"Name": "Alice", "Age": 20, "Grade": "A"},
        {"Name": "Bob", "Age": 21, "Grade": "B"},
        {"Name": "Charlie", "Age": 19, "Grade": "A"},
    ]
    
    formatter = Format3()
    result = formatter.format_data(student_data)
    print(result)
    print()
    
    # Example 2: Using custom delimiter
    print("Example 2: Custom Delimiter (::)")
    print("-" * 60)
    
    formatter2 = Format3(delimiter="::")
    result2 = formatter2.format_data(student_data)
    print(result2)
    print()
    
    # Example 3: Without padding
    print("Example 3: Without Padding")
    print("-" * 60)
    
    formatter3 = Format3(padding=False)
    result3 = formatter3.format_data(student_data)
    print(result3)
    print()
    
    # Example 4: Single item formatting
    print("Example 4: Single Item Format")
    print("-" * 60)
    
    single_item = {"ID": "12345", "Status": "Active", "Type": "Premium"}
    result4 = formatter.format_single(single_item)
    print(result4)
    print()
    
    # Example 5: Quick format function
    print("Example 5: Quick Format Function")
    print("-" * 60)
    
    product_data = [
        {"Product": "Laptop", "Price": "$999", "Stock": "15"},
        {"Product": "Mouse", "Price": "$25", "Stock": "50"},
        {"Product": "Keyboard", "Price": "$75", "Stock": "30"},
    ]
    
    result5 = format3_quick(product_data)
    print(result5)
    print()
    
    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
