# American Options Library
Demo of the Library that is supposed to use various methods to price options of american type.

### Installation
```
pip install american_options
```

### Get started
How to obtain option price with this library:

```Python
from american_options import Option

# Instantiate an Option object
option = Option(100, 100, 0.25, 1)

# Call the pricing method
result = option.european_call(0.05)
```
