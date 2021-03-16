"""
Matching Postal Codes:
    1.100000 - 999999
    2.Alternating digit shouldn't be repeated - more than 1 occurrence .
"""
regex_integer_in_range = r"[1-9]\d{5}$"  
regex_alternating_repetitive_digit_pair = r"(\d)(?=(\d)\1)"  
import re

P = input()
print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
