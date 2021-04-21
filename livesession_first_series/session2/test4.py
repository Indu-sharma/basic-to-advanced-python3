"""
Problem Statement:  Recommend for the better docstring in python script test3

Solution:
1. Remove the blank lines
2. Remove Unwanted Special chars.
3. Indentation
4. Unify the separators after part*
5. Append the Summary.
"""
import test3

summary = '\nSummary :: We concluded with __doc__ parsing'
print(test3.__doc__.strip().replace('    part', 'part').replace(':::', ' ').
      replace('  ', ' ').replace('==', '').replace('-', '::') + summary)
