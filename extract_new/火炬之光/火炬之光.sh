#!/bin/bash
# ============================================================================
# Torchlight: Rekindled -- Android arm64-v8a payload run by NextOS's own loader.
# The game is not recompiled: torchlight-loader dlopen()s the version-scrubbed
# libtorchlight.so through the private compat farm, fabricates the NativeActivity
# the payload's entry point reads, drives the Android lifecycle and hands it a
# synthetic AInputQueue.  farm/libEGL.so is the SDL presenter: it owns a real
# fullscreen window + GL context and blits the client's FBO to the panel.
#
# Layout: roms/ports/torchlight.sh + roms/ports/torchlight/{torchlight-loader,
# farm,libs.aarch64,gamedata}
# ============================================================================

XDG_DATA_HOME=${XDG_DATA_HOME:-$HOME/.local/share}

# ── PortMaster standard header ──
if [ -d "/opt/system/Tools/PortMaster/" ]; then
  controlfolder="/opt/system/Tools/PortMaster"
elif [ -d "/opt/tools/PortMaster/" ]; then
  controlfolder="/opt/tools/PortMaster"
elif [ -d "$XDG_DATA_HOME/PortMaster/" ]; then
  controlfolder="$XDG_DATA_HOME/PortMaster"
else
  controlfolder="/roms/ports/PortMaster"
fi

source $controlfolder/control.txt
source $controlfolder/device_info.txt

[ -f "${controlfolder}/mod_${CFW_NAME}.txt" ] && source "${controlfolder}/mod_${CFW_NAME}.txt"

get_controls

GAMEDIR=/$directory/ports/torchlight

> "$GAMEDIR/log.txt" && exec > >(tee "$GAMEDIR/log.txt") 2>&1

CONFDIR="$GAMEDIR/conf/"
$ESUDO mkdir -p "$CONFDIR" "$GAMEDIR/gamedata/save"

export XDG_CONFIG_HOME="$CONFDIR"
export XDG_DATA_HOME="$CONFDIR"

# The payload asks for Android-only entry names (libc.so, libm.so, libdl.so,
# libz.so, libandroid.so, liblog.so, libaaudio.so).  Real name-only provider
# files live in libs.aarch64/ and must come first: these firmwares ship GNU ld
# scripts under the short names and dlopen fails with "invalid ELF header".
# farm/ carries the compat layer, the EGL presenter and the GLES providers.
export LD_LIBRARY_PATH="$GAMEDIR/libs.aarch64:$GAMEDIR/farm:$LD_LIBRARY_PATH"

# Data root: the loader turns this into --ogre-media/--game-data/--console-ui.
# game_data.txt is what the Java layer used to write for the payload; the loader
# passes the same root on argv, but the client reads this file as well.
export TL_DATADIR="$GAMEDIR/gamedata"
printf '%s\n' "$TL_DATADIR" > "$GAMEDIR/gamedata/game_data.txt"

# Lifecycle switches: without them the loader only dlopens and reports.  The
# input queue is attached before APP_CMD_INIT_WINDOW because that is where the
# client launches its engine; RESUME runs on its own thread.
export TL_RUN_ENTRY=1
export TL_DRIVE_LIFECYCLE=1

# Panel geometry.  The presenter creates its SDL window at the size it is handed
# and this firmware's SDL fullscreen flag does not resize it (measured on the
# Oceanhorn port, 2026-10-21).  So the panel mode is read from DRM and passed in;
# built-in connectors win over an attached HDMI.  Unset means 1280x720.
torch_panel_mode() {
  local d m pass
  for pass in internal any; do
    for d in /sys/class/drm/card*-*/; do
      case "$d" in *Writeback*) continue ;; esac
      if [ "$pass" = internal ]; then
        case "$d" in *-DSI-*|*-eDP-*|*-LVDS-*|*-DPI-*) ;; *) continue ;; esac
      fi
      [ "$(cat "$d/status" 2>/dev/null)" = connected ] || continue
      m=$(head -1 "$d/modes" 2>/dev/null | grep -oE '^[0-9]+x[0-9]+')
      [ -n "$m" ] && { echo "$m"; return; }
    done
  done
}
panel=$(torch_panel_mode)
if [ -n "$panel" ]; then
  export TL_WIDTH="${panel%x*}"
  export TL_HEIGHT="${panel#*x}"
fi

# No video-backend exports: the front end already runs under sway and exports
# SDL_VIDEODRIVER=wayland with XDG_RUNTIME_DIR/WAYLAND_DISPLAY, and the presenter
# inherits them.  No audio exports: the AAudio shim dlopens the firmware SDL2
# and lets it pick the driver.

cd "$GAMEDIR"

# gptokeyb only provides the Select+Start quit.  The game reads the pad natively
# through the loader's evdev bridge, so torchlight.gptk unassigns every built-in
# key and mouse mapping.  The positional name is what the chord kills.
$GPTOKEYB "torchlight-loader" -c "$GAMEDIR/torchlight.gptk" &

SDL_GAMECONTROLLERCONFIG="$sdl_controllerconfig" ./torchlight-loader ./farm/libtorchlight_scrubbed.so ./farm

pm_finish
