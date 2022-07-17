# Generate a private and public key for ssh
# See https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key().public_bytes(
    serialization.Encoding.OpenSSH,
    serialization.PublicFormat.OpenSSH
)

# Output in OpenSSH format

openSSH = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.OpenSSH,
   # use BestAvailableEncryption is want password protected key
   #encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
   # Create key with no password
   encryption_algorithm=serialization.NoEncryption()
)


print(f"Private key: \n{openSSH}")
print(f"Public key: \n{public_key}")

# Write out private_key
with open("./private_key", "wb") as fp:
	fp.write(openSSH)

# Write out public_key
with open("./private_key.pub", "wb") as fp:
	fp.write(public_key)



