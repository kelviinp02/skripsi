"""
Format 3 - Data Formatting Module
This module provides functionality for Format 3 data processing.
"""


class Format3:
    """
    Format 3 data formatter.
    Converts data into Format 3 structure with specific formatting rules.
    """
    
    def __init__(self, delimiter="|", padding=True):
        """
        Initialize Format 3 formatter.
        
        Args:
            delimiter (str): The delimiter to use between fields (default: "|")
            padding (bool): Whether to add padding for alignment (default: True)
        """
        self.delimiter = delimiter
        self.padding = padding
    
    def format_data(self, data):
        """
        Format data according to Format 3 specifications.
        
        Args:
            data (list): List of dictionaries containing data to format
            
        Returns:
            str: Formatted string in Format 3 format
        """
        if not data:
            return ""
        
        # Get all keys from the first item
        keys = list(data[0].keys())
        
        # Calculate column widths if padding is enabled
        col_widths = {}
        if self.padding:
            for key in keys:
                col_widths[key] = max(
                    len(str(key)),
                    max(len(str(item.get(key, ""))) for item in data)
                )
        
        # Create header
        if self.padding:
            header = self.delimiter.join(
                str(key).ljust(col_widths[key]) for key in keys
            )
            separator = self.delimiter.join("-" * col_widths[key] for key in keys)
        else:
            header = self.delimiter.join(keys)
            separator = self.delimiter.join("-" * len(key) for key in keys)
        
        # Create data rows
        rows = []
        for item in data:
            if self.padding:
                row = self.delimiter.join(
                    str(item.get(key, "")).ljust(col_widths[key]) for key in keys
                )
            else:
                row = self.delimiter.join(str(item.get(key, "")) for key in keys)
            rows.append(row)
        
        # Combine all parts
        result = "\n".join([header, separator] + rows)
        return result
    
    def format_single(self, item):
        """
        Format a single data item in Format 3.
        
        Args:
            item (dict): Dictionary containing data to format
            
        Returns:
            str: Formatted string in Format 3 format
        """
        parts = []
        for key, value in item.items():
            parts.append(f"{key}: {value}")
        return self.delimiter + " ".join(parts) + self.delimiter


def format3_quick(data, delimiter="|"):
    """
    Quick function to format data using Format 3.
    
    Args:
        data (list): List of dictionaries to format
        delimiter (str): Delimiter to use (default: "|")
        
    Returns:
        str: Formatted string in Format 3 format
    """
    formatter = Format3(delimiter=delimiter)
    return formatter.format_data(data)
