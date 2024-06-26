from pycardano import *
from datetime import datetime, timedelta
import json

# Configuración de la red (por ejemplo, para la red de prueba)
network = Network.TESTNET

# Configuración del backend
context = BlockFrostChainContext(
    project_id="your_blockfrost_project_id",  # Reemplaza con tu Project ID de BlockFrost
    base_url=ApiUrls.testnet.value
)

# Direcciones y claves
sender_address = Address.from_primitive("your_sender_address")  # Reemplaza con tu dirección
sender_skey = PaymentSigningKey.load("path_to_your_payment.skey")  # Reemplaza con la ruta a tu archivo .skey

# Script de política
policy_signing_key = PaymentSigningKey.load("path_to_policy.skey")  # Reemplaza con la ruta a tu archivo .skey
policy_verification_key = PaymentVerificationKey.from_signing_key(policy_signing_key)
policy_script = ScriptPubkey(policy_verification_key.hash())

# Política de acuñación con fecha de vencimiento
valid_until = int((datetime.utcnow() + timedelta(days=1)).timestamp())  # Válido por un día
policy = ScriptAll([policy_script, InvalidBefore(valid_until)])

policy_id = policy.id

# Detalles del NFT
asset_name = "MyNFT"  # Reemplaza con el nombre de tu NFT
token_amount = 1  # Cantidad de tokens a acuñar (1 para NFT)

# Leer metadatos desde el archivo JSON
with open("nft_metadata.json", "r") as f:
    metadata = json.load(f)

# Crear transacción
builder = TransactionBuilder(context)

# Añadir utxo de entrada
utxos = context.utxos(sender_address)
builder.add_input_address(sender_address)

# Construir la salida con el NFT acuñado
output = TransactionOutput(
    address=sender_address,
    amount=[
        TransactionOutput.from_primitive([str(sender_address), 2_000_000]),  # Min. ADA requerido en la salida
        TransactionOutput.from_primitive([str(policy_id), {asset_name: token_amount}])
    ]
)

builder.add_output(output)

# Añadir testigo de política
builder.mint = {AssetName(asset_name): token_amount}
builder.native_scripts = [policy]

# Añadir metadatos
builder.auxiliary_data = AuxiliaryData(AlonzoMetadata(metadata))

# Construir y firmar la transacción
tx_body = builder.build(change_address=sender_address)
tx = Transaction(tx_body, [sender_skey, policy_signing_key])

# Enviar transacción
context.submit_tx(tx.to_cbor())

print(f"Transacción enviada con ID: {tx.id}")
