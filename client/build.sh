#!/usr/bin/env bash
# exit on error
#set -o errexit
cd /client
# Instalar dependencias
#npm install --save-dev lerna
yarn install
# Ejecutar servidor react
npm run build