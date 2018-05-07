def apply_discount(product, discount):
    """However, the assertions should be used very carefully & only in non-business impacting cases. Reason: Python
assertions can be disabled at interpreter level by using -O (Disables the Debugging) and -OO(Disables docstring)
command line switches as well as PYTHONOPTIMIZE environment variable as a result assert statements wont be
evaluated. Example: python -O <my-program>.py ; it prints only the doc & assert statement means nothing. Example:
python -OO <my-program>.py ; it disables the effect of assert statements as well as the docstring. Python checks
disable/enable assert statements with bool __debug__ ,which is set to False incase of using -O or -OO flags. """

    price = int(product['price']) * (1.0 - discount)
    assert 0 <= price <= product['price'], "Price of the product after discount is less than Zero!"
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14800}

print(apply_discount(shoes, 1.0))
print(apply_discount.__doc__)


# Never use the assert with tuple object.

test = 11
assert (test == 10, 'It may seem to raise assertion error; but the tuple object always evaluates to True')
