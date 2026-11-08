#!/bin/bash
# muOS audio workaround based on Mikhail/Crescent's adaptation.
audio_active=0;pw_running=0;wp_running=0;original_volume="";volume_pid=""
hardware_mixer(){ (unset ALSA_CONFIG_PATH ALSA_CARD; amixer "$@"); }
start_muos_audio(){
 [ -d /opt/muos ] || return 0
 audio_active=1
 command -v pgrep >/dev/null || { printf 'muOS: pgrep missing; cannot manage audio services\n'; return 0; }
 pgrep -x pipewire >/dev/null && pw_running=1
 pgrep -x wireplumber >/dev/null && wp_running=1
 original_volume=$(hardware_mixer -c 0 get 'digital volume' 2>/dev/null | awk '/Mono:/ {print $2;exit}') || true
 [ "$wp_running" = 0 ] || pkill -TERM -x wireplumber || true
 [ "$pw_running" = 0 ] || pkill -TERM -x pipewire || true
 for ((n=0;n<30;n++)); do
  if ! pgrep -x pipewire >/dev/null && ! pgrep -x wireplumber >/dev/null; then break; fi
  sleep 0.1
 done
 export SDL_AUDIODRIVER=alsa SDL_AUDIODEV=asphalt6 ALSA_CONFIG_PATH="$GAMEDIR/alsa-asphalt6.conf" ALSA_CARD=0
 if command -v python3 >/dev/null && command -v amixer >/dev/null; then
  python3 "$GAMEDIR/tools/volume-hook.py" & volume_pid=$!
 fi
 printf 'muOS direct ALSA: card=0 device=0 PipeWire=%s WirePlumber=%s volume=%s\n' "$pw_running" "$wp_running" "$original_volume"
}
restore_muos_audio(){
 [ "$audio_active" = 1 ] || return 0
 audio_active=0
 if [ -n "$volume_pid" ]; then kill -TERM "$volume_pid" 2>/dev/null || true; wait "$volume_pid" 2>/dev/null || true; fi
 # Keep game-specific ALSA overrides out of the restarted desktop services.
 if [ "$pw_running" = 1 ] && ! pgrep -x pipewire >/dev/null; then
  (unset ALSA_CONFIG_PATH ALSA_CARD SDL_AUDIODEV SDL_AUDIODRIVER; exec pipewire -c /opt/muos/share/conf/pipewire.conf) &
  sleep 1
 fi
 if [ "$wp_running" = 1 ] && ! pgrep -x wireplumber >/dev/null; then
  (unset ALSA_CONFIG_PATH ALSA_CARD SDL_AUDIODEV SDL_AUDIODRIVER; exec wireplumber) &
  sleep 1
 fi
 [ -z "$original_volume" ] || hardware_mixer -c 0 set 'digital volume' "$original_volume" || true
 printf 'muOS audio restored\n'
}
