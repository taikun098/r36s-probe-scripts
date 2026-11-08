#!/bin/bash
set -euo pipefail
root=$1
shader="$root/gamefiles/sdcard/gameloft/games/GloftA6HP/file000460.dat"
payload="$root/tools/roadlm-test20.dat"
original=e5ab49c09f4b6594db627877593ea1bf0e3cecab3d26a573a13e9bcb40896ec1
patched=c1cefc1032fb7615270cd2d64dbd92a9ec7aec0c35ce84f109e1a86d26e0c514
actual=$(sha256sum -- "$shader"); actual=${actual%% *}
if [ "$actual" = "$patched" ]; then
 echo 'SETUP_ROAD_FIX test20 already_applied'; exit 0
fi
[ "$actual" = "$original" ] || { echo 'SETUP_ROAD_FIX_ERROR unknown RoadLM shader'; exit 1; }
actual=$(sha256sum -- "$payload"); actual=${actual%% *}
[ "$actual" = "$patched" ] || { echo 'SETUP_ROAD_FIX_ERROR damaged patch payload'; exit 1; }
[ "$(wc -c < "$shader")" = "$(wc -c < "$payload")" ] || exit 1
tmp=$(mktemp "${shader}.test20-XXXXXX")
trap 'rm -f -- "$tmp"' EXIT
cp -- "$payload" "$tmp"
actual=$(sha256sum -- "$tmp"); actual=${actual%% *}
[ "$actual" = "$patched" ] || exit 1
mv -f -- "$tmp" "$shader"
echo 'SETUP_ROAD_FIX test20 applied specular_disabled=RoadLM'
