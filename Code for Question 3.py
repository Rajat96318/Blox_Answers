# Note : You can run the code in Jupyter notebook or Google Colab or visual studio
# first install one package
# pip install simplejson

# In this the integer and float have arbitrary precisions
# I have used different datatypes

import json
import simplejson
from decimal import Decimal

json_string = '{"string": "Hello, world!", "number": 42123456789098765432123456789,"float": 1234567890123456789012345678901234567890.1234567890123456789012345678901234567890,"boolean": true,"null_value": null,"array": [1, 2, 3, "four", 5.5],"object": {"key1": "value1","key2": 42,"key3": [true, false, null]}}'

dct = json.loads(json_string, parse_float=Decimal)

print(simplejson.dumps(dct, use_decimal=True))

