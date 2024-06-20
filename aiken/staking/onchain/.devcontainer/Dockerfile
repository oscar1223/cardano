FROM ubuntu:22.04
RUN apt update && \
    apt install -y curl less build-essential tree
RUN curl --proto '=https' --tlsv1.2 -LsSf https://install.aiken-lang.org | sh
RUN $HOME/.aiken/bin/aikup
