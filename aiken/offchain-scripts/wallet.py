from pycardano import PaymentKeyPair, StakeKeyPair, Address, Network
from mnemonic import Mnemonic
import os

# Generar las frases semilla utilizando la librería 'mnemonic'
mnemo = Mnemonic("english")
seed_phrase = mnemo.generate(strength=256)  # Genera una frase de 24 palabras

# Convertir la frase semilla a una semilla binaria
seed = mnemo.to_seed(seed_phrase)

# Generar una nueva clave de pago y su correspondiente clave pública usando la semilla
payment_key_pair = PaymentKeyPair.from_seed(seed)

# Guardar la clave privada y pública en archivos
payment_skey_path = "payment.skey"
payment_vkey_path = "payment.vkey"

payment_key_pair.signing_key.save(payment_skey_path)
payment_key_pair.verification_key.save(payment_vkey_path)

# Generar una nueva clave de staking y su correspondiente clave pública usando la semilla
staking_key_pair = StakeKeyPair.from_seed(seed)

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

# Guardar la frase semilla en un archivo
seed_phrase_path = "seed_phrase.txt"
with open(seed_phrase_path, "w") as f:
    f.write(seed_phrase)

print("Billetera creada con éxito")
print(f"Dirección: {address}")
print(f"Clave privada de pago guardada en: {payment_skey_path}")
print(f"Clave pública de pago guardada en: {payment_vkey_path}")
print(f"Clave privada de staking guardada en: {staking_skey_path}")
print(f"Clave pública de staking guardada en: {staking_vkey_path}")
print(f"Dirección guardada en: {address_path}")
print(f"Frase semilla guardada en: {seed_phrase_path}")
