import sys

from .v1 import encode

if __name__ == "__main__":
    try:
        value_to_encode = int(sys.argv[1])
        encoded_value = encode(value_to_encode)
        print(encoded_value)
    except Exception:
        print("Usage: alphinity [value_to_encode]")
        sys.exit(1)
