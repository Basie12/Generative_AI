#!/bin/bash
set -e

BOOTCAMP=~/Generative_AI_Modern_Route/Full-Stack-GenAI-Bootcamp-1.0
MYREPO=~/Generative_AI_Modern_Route/Generative_AI

echo "Pulling latest bootcamp updates..."
cd "$BOOTCAMP"
git pull origin main

echo "Syncing ALL class folders..."
rm -rf "$MYREPO/notebooks/bootcamp"/*
cp -r "$BOOTCAMP"/Class-* "$MYREPO/notebooks/bootcamp/"

echo "Done!"