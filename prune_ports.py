import os, re
root=r"E:\ports"
# Selected "great/classic" ports (exact gamelist names)
SELECT = set("""
Cave Story
Cave Story-evo
Doom 3
Doom Engines
Quake 3
Duke Nukem 3D
Blood
Shadow Warrior
Marathon
Marathon 2
Marathon Infinity
Perfect Dark
Hexen 2 - Portal of Praevus
Celeste Classic
Celeste64
Spelunky
Super Crate Box
C-Dogs
Cannonball
SDLPoP
OpenJazz
SRB2
Sonic Robo Blast 2 Kart
Sonic 1
Sonic 2
Sonic CD
Sonic Mania
Jazz2 Resurrection
OpenTTD
OpenRA
VanillaRA
VanillaTD
Battle for Wesnoth
FreeCiv
Minetest
OpenRCT2
Warzone 2100
Widelands
Mindustry
Dune Legacy
Seven Kingdoms - Ancient Adversaries
OpenXcomEX
CorsixTH
Shattered Pixel Dungeon
Fallout 1
Fallout 2
Deltarune
Devilutionx
Ultima VI (Nuvie Engine)
FreeDink
Dungeon Crawl Stone Soup
Angband
Brogue
Trigger Rally
Xmoto
Ultimate Stunts
OpenSupaplex
2048
Neverball
Frozen Bubble
""".strip().splitlines())

# remove whitespace entries
SELECT=set(s.strip() for s in SELECT if s.strip())
print("selected count:",len(SELECT))

# list all .sh in ports root
sh_files=[f for f in os.listdir(root) if f.endswith('.sh')]
print("root .sh before:",len(sh_files))

kept=[]; removed=0
for f in sh_files:
    name=os.path.splitext(f)[0]
    if name in SELECT:
        kept.append(f)
    else:
        os.remove(os.path.join(root,f))
        removed+=1

print("removed .sh:",removed)
print("kept .sh:",len(kept))

# rebuild gamelist.xml with kept only
lines=['<?xml version="1.0" encoding="UTF-8"?>','<gameList>']
for f in sorted(kept):
    name=os.path.splitext(f)[0]
    lines.append('  <game>')
    lines.append('    <path>./%s</path>'%f)
    lines.append('    <name>%s</name>'%name)
    lines.append('    <desc></desc>')
    lines.append('  </game>')
lines.append('</gameList>')
open(os.path.join(root,'gamelist.xml'),'w',encoding='utf-8').write('\n'.join(lines))
print("gamelist.xml rebuilt with",len(kept),"games")
# report kept
print("=== KEPT GAMES ===")
for f in sorted(kept):
    print("  ",os.path.splitext(f)[0])
