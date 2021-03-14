import base64

import javaobj.v2 as javaobj

with open(".cobaltstrike.beacon_keys", "rb") as fd:
    pobj = javaobj.load(fd)
privateKey = pobj.array.value.privateKey.encoded.data
publicKey = pobj.array.value.publicKey.encoded.data


privateKey = (
    b"-----BEGIN PRIVATE KEY-----\n"
    + base64.encodebytes(bytes(map(lambda x: x & 0xFF, privateKey)))
    + b"-----END PRIVATE KEY-----"
)
publicKey = (
    b"-----BEGIN PUBLIC KEY-----\n"
    + base64.encodebytes(bytes(map(lambda x: x & 0xFF, publicKey)))
    + b"-----END PUBLIC KEY-----"
)
print(privateKey.decode())
print(publicKey.decode())

# print(
#     list(
#         map(
#             lambda x: list(map(lambda y: (y[0].name, y[1]), x.items())),
#             a.field_data.values(),
#         )
#     )
# )
