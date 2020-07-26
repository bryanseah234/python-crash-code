#mostdestructive
import ctypes
p = ctypes.pointer(ctypes.c_char.from_address(5))
while True:
  p[0] = b'x'
  p = p + 1
