"""
This is a Configuration file for your Test Setups.
"""


class Config:
    def __init__(self, environment):
        self.my_env = {
            'qa': 'https://www.facebook.com/',
            'dev': 'https://www.google.com/'
        }[environment]
