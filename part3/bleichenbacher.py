from roots import *
import hashlib
import sys
message = sys.argv[1]

# Your code to forge a signature goes here.
n = 0x00bbcc67e6218f02a9b5e358cf36cf1ef3ea76f32bb3645f1de2212beba2f6fd181cdc855ba681c301bfeac7dbbf1c783a578f0568d1869a310c2e40fc9fab5579
e = 3
m = hashlib.sha256()
m.update(message)
# print m.hexdigest()
t = int(m.hexdigest(), 16)
head = 0x0001FF003031300d060960864801650304020105000420
fake_int = (head * pow(2,256) + t)*pow(2,201*8)
# print str(hex(fake_int))
result = integer_nthroot(fake_int,e)
forged_signature = result[0]
good = result[1]
if not good:
    forged_signature += 1

# print forged_signature
# print good
# print hex(pow(forged_signature,e))
print integer_to_base64(forged_signature)