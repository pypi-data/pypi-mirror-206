# alphinity

alphinity encodes integers to alphabetize in ascending order.

```python3
from alphinity import encode

encode(100)  # -> "ccv"

# passes
assert sorted(map(encode, range(10**6))) == [*map(encode, range(10**6))]
```

For stable encoding,
```python3
from alphinity.v1 import encode
```

## Notes

Alphabetization doesn't work strictly infinitely, just through very, very high integers i.e., `1e35`.

Non-negative integers only.
