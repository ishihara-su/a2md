#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a2md.py - Create a markdown file from a file or a URL
Susumu Ishihara
Created on Apr. 28, 2025
"""

from markitdown import MarkItDown
import sys

if __name__ == "__main__":
    # Check if the user provided a file or URL as an argument
    if len(sys.argv) < 2:
        print("Usage: python a2md.py <file_or_url>")
        sys.exit(1)

input_file_or_url = sys.argv[1]
md = MarkItDown()
result = md.convert(input_file_or_url)
print(result.text_content)
