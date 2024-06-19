# Usa una imagen base con Ubuntu
FROM ubuntu:20.04

# Establece la variable de entorno para desactivar las preguntas interactivas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza y instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates

# Agrega el repositorio de IOHK
RUN curl -sS https://updates.cardano.org/daedalus/release/KEY.gpg | apt-key add - && \
    echo "deb [arch=amd64] https://updates.cardano.org/daedalus/release/ bionic main" | tee /etc/apt/sources.list.d/daedalus.list

# Instala cardano-wallet
RUN apt-get update && apt-get install -y cardano-wallet

# Configura el comando de inicio del contenedor
CMD ["cardano-wallet", "serve", "--node-socket", "/home/cardano/cardano-my-node/db/socket", "--database", "/home/cardano/cardano-my-node/db", "--port", "8090"]