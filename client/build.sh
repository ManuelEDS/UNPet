#!/usr/bin/env bash
# exit on error
set -o errexit
# Instalar dependencias
npm install
# Ejecutar servidor react
npm run build