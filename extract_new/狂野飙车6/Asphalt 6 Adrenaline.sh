#!/bin/bash
# Asphalt 6 v1.3.3 BYO-DATA launcher. Place this file beside asphalt6/ in ports/.
set -u
PORT_ROOT=$(cd -- "$(dirname -- "$0")" && pwd)
# muOS can keep its menu launcher separately from the port data.
if [ -d "$PORT_ROOT/asphalt6" ]; then
 cd "$PORT_ROOT/asphalt6" || exit 1
elif [ -d /opt/muos ]; then
 for candidate in /mnt/sdcard/ports/asphalt6 /mnt/mmc/ports/asphalt6 /mnt/sdcard/ROMS/Ports/asphalt6 /mnt/mmc/ROMS/Ports/asphalt6; do
  [ ! -d "$candidate" ] || { cd "$candidate" || exit 1; break; }
 done
 [ -f ./asphalt6 ] || exit 1
else
 exit 1
fi
GAMEDIR=$PWD
mkdir -p logs runtime-libs
LOG="$GAMEDIR/logs/asphalt6-$(date +%Y%m%d-%H%M%S)-$$.log"
exec >"$LOG" 2>&1
printf '=== Asphalt 6 ARM Linux test17 APK in data ===\n'
date -Is
uname -a
export LD_LIBRARY_PATH="$PWD/runtime-libs:/usr/lib32:/usr/lib/arm-linux-gnueabihf:/lib/arm-linux-gnueabihf${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
for pair in 'libEGL.so.1:libEGL.so' 'libGLESv2.so.2:libGLESv2.so'; do
 soname=${pair%%:*};basename=${pair#*:}
 for dir in /usr/lib32 /usr/lib/arm-linux-gnueabihf /lib/arm-linux-gnueabihf /usr/lib; do
  candidate="$dir/$basename";[ -f "$candidate" ] || continue
  if command -v readelf >/dev/null && readelf -h "$candidate" 2>/dev/null | grep -q 'Class:.*ELF32'; then
   ln -sf "$candidate" "runtime-libs/$soname";break
  fi
 done
done
chmod +x ./asphalt6 tools/a6-setup tools/a6-status 2>/dev/null || true
ui_pid="";stage="";locked=0;game_pid=""
source "$GAMEDIR/tools/muos-audio.sh"
stop_ui(){ if [ -n "$ui_pid" ];then kill -TERM "$ui_pid" 2>/dev/null || true;wait "$ui_pid" 2>/dev/null || true;ui_pid="";fi; }
cleanup(){
 if [ -n "$game_pid" ] && kill -0 "$game_pid" 2>/dev/null; then
  kill -TERM "$game_pid" 2>/dev/null || true
  for ((i=0;i<30;i++)); do kill -0 "$game_pid" 2>/dev/null || break; sleep 0.1; done
  kill -KILL "$game_pid" 2>/dev/null || true
  wait "$game_pid" 2>/dev/null || true
 fi
 restore_muos_audio
 stop_ui;[ -z "$stage" ] || rm -rf -- "$stage";if [ "$locked" = 1 ];then rm -f .setup-lock/pid;rmdir .setup-lock 2>/dev/null || true;fi; }
trap cleanup EXIT
trap 'exit 130' INT TERM HUP
show(){ printf '%s\n%s\n' "$1" "$2";tools/a6-status "$1" "$2" "$3" || true; }
failed(){ stop_ui;printf 'EXTRACTION_FAILED: %s\nError log: %s\n' "$1" "$LOG";show 'Extraction failed' 'See asphalt6/logs for details' 8;exit 1; }
# Exclude concurrent setup/game runs; recover a stale lock after a reboot.
if ! mkdir .setup-lock 2>/dev/null;then
 old_pid=$(cat .setup-lock/pid 2>/dev/null || true)
 if [[ "$old_pid" =~ ^[0-9]+$ ]] && kill -0 "$old_pid" 2>/dev/null;then
  show 'Asphalt 6 is already running' 'Please close the other instance' 5;exit 1
 fi
 rm -f .setup-lock/pid;rmdir .setup-lock 2>/dev/null || failed 'Cannot recover setup lock'
 mkdir .setup-lock || failed 'Cannot acquire setup lock'
fi
locked=1;echo $$ > .setup-lock/pid
# The current launch plus the two most recently modified previous logs.
shopt -s nullglob
log_files=("$GAMEDIR/logs"/asphalt6-*.log)
kept=0
while IFS= read -r old_log; do
 [ "$old_log" != "$LOG" ] || continue
 if [ "$kept" -lt 2 ]; then kept=$((kept+1)); else rm -f -- "$old_log"; fi
done < <(ls -1t -- "${log_files[@]}" 2>/dev/null)
# Remove only the obsolete per-launch backup directory, never live saves.
rm -rf -- "$GAMEDIR/logs/save-backups"
ready=0
if [ -f .byodata-ready ] && tools/a6-setup --check "$GAMEDIR";then ready=1;fi
if [ "$ready" = 0 ];then
 shopt -s nullglob nocaseglob
 apks=("$GAMEDIR/data"/*.apk)
 [ "${#apks[@]}" -eq 1 ] || failed 'Place exactly one correct Asphalt 6 v1.3.3 APK in asphalt6/data/'
 [ -d data ] || failed 'Place the extracted game cache folder inside asphalt6/data/'
 stage=$(mktemp -d "$GAMEDIR/.setup-XXXXXX") || failed 'Cannot create temporary setup folder'
 printf 'Extracting game data...\n'
 tools/a6-status 'Extracting game data...' 'Please wait - do not power off' 0 & ui_pid=$!
 if ! tools/a6-setup "${apks[0]}" "$GAMEDIR/data" "$stage";then failed 'APK/cache validation or extraction failed';fi
 stop_ui
 # Preserve previous progress when migrating from test01 or repairing setup.
 oldsd="$GAMEDIR/gamefiles/sdcard/gameloft/games/GloftA6HP"
 newsd="$stage/gamefiles/sdcard/gameloft/games/GloftA6HP"
 for save in "$oldsd"/profile*.sav "$oldsd"/profile*.bak;do [ ! -f "$save" ] || cp -p -- "$save" "$newsd/" || failed 'Cannot preserve save';done
 oldprefs="$GAMEDIR/gamefiles/data/data/com.gameloft.android.ANMP.GloftA6HP/shared_prefs"
 newprefs="$stage/gamefiles/data/data/com.gameloft.android.ANMP.GloftA6HP/shared_prefs"
 for pref in "$oldprefs"/*.xml;do [ ! -f "$pref" ] || cp -p -- "$pref" "$newprefs/" || failed 'Cannot preserve preferences';done
 # Keep an existing prepared installation as a backup; rollback if commit fails.
 backup=""
 if [ -d gamefiles ];then
  backup="$GAMEDIR/.previous-gamefiles-$(date +%Y%m%d-%H%M%S)-$$"
  mv -- gamefiles "$backup" || failed 'Cannot back up existing game data'
 fi
 if ! mv -- "$stage/gamefiles" "$GAMEDIR/gamefiles";then
  [ -z "$backup" ] || mv -- "$backup" "$GAMEDIR/gamefiles"
  failed 'Cannot install prepared game data'
 fi
 if ! mv -- "$stage/libasphalt6.so" "$GAMEDIR/libasphalt6.so";then failed 'Cannot install game library';fi
 printf 'Asphalt 6 v1.3.3 BYO-DATA setup schema 1\n' > .byodata-ready || failed 'Cannot record setup completion'
 [ -z "$backup" ] || rm -rf -- "$backup"
 rm -rf -- "$stage";stage=""
 show 'Extraction complete' 'Starting Asphalt 6...' 2
fi
# Private test distribution: bundled, verified supplemental vehicle assets.
if ! tools/a6-setup --check-cars "$GAMEDIR";then
 [ -f "$GAMEDIR/tools/vehicle-fix.zip" ] || failed 'Bundled vehicle-fix.zip is missing; reinstall the complete port package'
 tools/a6-status 'Installing vehicle data' 'Please wait...' 0 & ui_pid=$!
 if ! tools/a6-setup --repair-cars "$GAMEDIR/tools/vehicle-fix.zip" "$GAMEDIR";then failed 'Vehicle data installation failed';fi
 stop_ui
 show 'Vehicle data installation complete' 'Starting Asphalt 6...' 2
fi
# Apply after extraction and on upgrades; same-size validated shader patch.
if ! bash "$GAMEDIR/tools/road-fix.sh" "$GAMEDIR"; then failed 'New York shader patch failed; see SETUP_ROAD_FIX_ERROR in log'; fi
# Normal logs remain enabled; verbose diagnostics are opt-in.
export A6_PERF_LOG=${A6_PERF_LOG:-0} A6_INPUT_DIAG=${A6_INPUT_DIAG:-0} A6_TEX_DIAG=${A6_TEX_DIAG:-0} A6_PADCAL=${A6_PADCAL:-0} A6_RENDER_DIAG=${A6_RENDER_DIAG:-0}
start_muos_audio
# Diagnostic test: frame timing and FPS, once per 120 presentations.
if [ -d /opt/muos ]; then export A6_PERF_DETAIL=${A6_PERF_DETAIL:-1}; fi
printf 'GAME_START SDL video=%s audio=%s\n' "${SDL_VIDEODRIVER:-auto}" "${SDL_AUDIODRIVER:-auto}"
./asphalt6 &
game_pid=$!
wait "$game_pid"
status=$?
game_pid=""
printf 'Game exit status=%s\n' "$status"
exit "$status"
