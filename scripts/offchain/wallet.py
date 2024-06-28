from pycardano import PaymentSigningKey, PaymentVerificationKey, StakeSigningKey, StakeVerificationKey, Address, Network
from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import os

# Generar las frases semilla utilizando la librería 'mnemonic'
mnemo = Mnemonic("english")
seed_phrase = mnemo.generate(strength=256)  # Genera una frase de 24 palabras

# Convertir la frase semilla a una semilla binaria
seed = mnemo.to_seed(seed_phrase)

# Utilizar bip-utils para generar claves a partir de la semilla
seed_generator = Bip39SeedGenerator(seed_phrase)
bip44_mst = Bip44.FromSeed(seed_generator.Generate(), Bip44Coins.CARDANO_BYRON_ICARUS)
bip44_acc = bip44_mst.Purpose().Coin().Account(0)
bip44_chg = bip44_acc.Change(Bip44Changes.CHAIN_EXT)

payment_key_pair = bip44_chg.AddressIndex(0)
staking_key_pair = bip44_chg.AddressIndex(1)

# Convertir las claves a las clases correspondientes de pycardano
payment_signing_key = PaymentSigningKey(payment_key_pair.PrivateKey().Raw().ToBytes())
payment_verification_key = PaymentVerificationKey(payment_key_pair.PublicKey().RawCompressed().ToBytes())

staking_signing_key = StakeSigningKey(staking_key_pair.PrivateKey().Raw().ToBytes())
staking_verification_key = StakeVerificationKey(staking_key_pair.PublicKey().RawCompressed().ToBytes())

# Guardar las claves privadas y públicas en archivos
payment_skey_path = "payment.skey"
payment_vkey_path = "payment.vkey"

payment_signing_key.save(payment_skey_path)
payment_verification_key.save(payment_vkey_path)

# Guardar las claves de staking en archivos
staking_skey_path = "staking.skey"
staking_vkey_path = "staking.vkey"

staking_signing_key.save(staking_skey_path)
staking_verification_key.save(staking_vkey_path)

# Crear la dirección de la billetera
address = Address(payment_verification_key.hash(), staking_verification_key.hash(), network=Network.TESTNET)

# Guardar la dirección en un archivo
address_path = "address.txt"
with open(address_path, "w") as f:
    f.write(str(address))

# Guardar la frase semilla en un archivo
seed_phrase_path = "seed_phrase.txt"
with open(seed_phrase_path, "w") as f:
    f.write(seed_phrase)

# Generar claves de política
policy_signing_key = PaymentSigningKey.generate()
policy_verification_key = PaymentVerificationKey.from_signing_key(policy_signing_key)

# Guardar las claves de política en archivos
policy_skey_path = "policy.skey"
policy_vkey_path = "policy.vkey"

with open(policy_skey_path, "w") as skey_file:
    skey_file.write(str(policy_signing_key))

with open(policy_vkey_path, "w") as vkey_file:
    vkey_file.write(str(policy_verification_key))

print("Billetera creada con éxito")
print(f"Dirección: {address}")
print(f"Clave privada de pago guardada en: {payment_skey_path}")
print(f"Clave pública de pago guardada en: {payment_vkey_path}")
print(f"Clave privada de staking guardada en: {staking_skey_path}")
print(f"Clave pública de staking guardada en: {staking_vkey_path}")
print(f"Dirección guardada en: {address_path}")
print(f"Frase semilla guardada en: {seed_phrase_path}")
print(f"Clave privada de política guardada en: {policy_skey_path}")
print(f"Clave pública de política guardada en: {policy_vkey_path}")
