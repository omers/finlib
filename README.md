# finpredict python package
##
Example
```python
from finpredict import FinData

data = FinData()

df = data.get_stock('MSFT', start='2015-01', end='2021-04')
print(df.tail())
```