#!/usr/bin/env bash
# exit on error
#set -o errexit
cd /client
# Instalar dependencias
yarn install
# Ejecutar servidor react
npm run build