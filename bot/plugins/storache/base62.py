import string


BASE62_ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase
BASE62_BASE = len(BASE62_ALPHABET)

def base62_encode(value):
  """Encode a number to a base62 string."""
  if value == 0:
      return BASE62_ALPHABET[0]

  encoded = []
  while value:
      value, rem = divmod(value, BASE62_BASE)
      encoded.append(BASE62_ALPHABET[rem])

  return ''.join(reversed(encoded))

def base62_decode(encoded):
  """Decode a base62 string to a number."""
  value = 0
  for char in encoded:
      value = value * BASE62_BASE + BASE62_ALPHABET.index(char)
  return value

def bytes_to_base62(data):
  """Encode bytes to a base62 string."""
  # Convert bytes to integer
  value = int.from_bytes(data, byteorder='big')
  return base62_encode(value)

def base62_to_bytes(encoded):
  """Decode a base62 string to bytes."""
  # Decode base62 to integer
  value = base62_decode(encoded)
  # Convert integer to bytes
  length = (value.bit_length() + 7) // 8
  return value.to_bytes(length, byteorder='big')
