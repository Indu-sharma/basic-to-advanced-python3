from __future__ import print_function
from pprint import pprint
import yaml

stream = file("corelation.yaml")
mydict = yaml.safe_load(stream=stream)
pprint(mydict)
