#!/usr/bin/env bash

set -euo pipefail

script_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
lib_directory="$script_directory/src/lib"

mkdir -p "$lib_directory"

# microdot 1.2.0
echo "Downloading microdot..."
curl --silent --output-dir "$lib_directory" \
  --remote-name https://raw.githubusercontent.com/miguelgrinberg/microdot/v1.2.0/src/microdot.py \
  --remote-name https://raw.githubusercontent.com/miguelgrinberg/microdot/v1.2.0/src/microdot_asyncio.py \
  --remote-name https://raw.githubusercontent.com/miguelgrinberg/microdot/v1.2.0/src/microdot_asyncio_websocket.py \
  --remote-name https://raw.githubusercontent.com/miguelgrinberg/microdot/v1.2.0/src/microdot_websocket.py
