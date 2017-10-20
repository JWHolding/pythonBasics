import time, hmac, base64, hashlib, struct

def dynamic_truncate(raw_bytes, length):
    """Per https://tools.ietf.org/html/rfc4226#section-5.3"""
    offset = ord(raw_bytes[19]) & 0x0f
    decimal_value = ( ord(raw_bytes[offset]) & 0x7f) << 24 | ord(raw_bytes[offset+1]) << 16 | ord(raw_bytes[offset+2]) << 8 | ord(raw_bytes[offset+3]) return str(decimal_value)[-length:] def pack_time(counter): """Converts integer time into bytes""" return struct.pack(">Q", counter)

secret32='abcdefghijklmnop'
secret_bytes = base64.b32decode(secret32.upper())

counter = int(time.time())/30
counter = pack_time(counter)

raw_hmac = hmac.new(secret_bytes, counter, hashlib.sha1).digest()
print dynamic_truncate(raw_hmac, 6)

## Verify, if you have oathtool installed
import os
os.system("oathtool --totp -b '%s'" % secret32)
