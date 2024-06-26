from pycardano import PaymentKeyPair, StakeKeyPair, Address
import os

# Generar una nueva clave de pago y su correspondiente clave pública
payment_key_pair = PaymentKeyPair.generate()

# Guardar la clave privada y pública en archivos
payment_skey_path = "payment.skey"
payment_vkey_path = "payment.vkey"

payment_key_pair.signing_key.save(payment_skey_path)
payment_key_pair.verification_key.save(payment_vkey_path)

# Generar una nueva clave de staking y su correspondiente clave pública
staking_key_pair = StakeKeyPair.generate()

# Guardar la clave privada y pública en archivos
staking_skey_path = "staking.skey"
staking_vkey_path = "staking.vkey"

staking_key_pair.signing_key.save(staking_skey_path)
staking_key_pair.verification_key.save(staking_vkey_path)

# Crear la dirección de la billetera
address = Address(payment_key_pair.verification_key.hash(), staking_key_pair.verification_key.hash(), network=Network.TESTNET)

# Guardar la dirección en un archivo
address_path = "address.txt"
with open(address_path, "w") as f:
    f.write(str(address))

print("Billetera creada con éxito")
print(f"Dirección: {address}")
print(f"Clave privada de pago guardada en: {payment_skey_path}")
print(f"Clave pública de pago guardada en: {payment_vkey_path}")
print(f"Clave privada de staking guardada en: {staking_skey_path}")
print(f"Clave pública de staking guardada en: {staking_vkey_path}")
print(f"Dirección guardada en: {address_path}")
