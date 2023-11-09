#!/usr/bin/env bash
set -o errexit
# Instalar dependencias y
# Ejecutar servidor react
npm install -g yarn --force
yarn install --frozen-lockfile   
yarn build