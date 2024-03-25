#!/bin/bash


SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

ENV_FILE=".env"

if [ ! -f "$ENV_FILE" ]; then
    touch "$ENV_FILE"
    echo "Created $ENV_FILE"
fi

echo "SECRET_KEY=$SECRET_KEY" >> "$ENV_FILE"
echo "Added SECRET_KEY to $ENV_FILE"
