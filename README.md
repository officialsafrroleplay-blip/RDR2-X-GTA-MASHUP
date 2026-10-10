# Gunslingers & Getaway Cars (RDR2 x GTA V) — design stage, NOT built or tested

Play Red Dead Redemption 2 **story mode** (host game) as Arthur Morgan with RDR2's physics and animations.
A key (F6) opens an arsenal menu: spawn GTA V cars (Sultan, Adder, Bison pickup), take GTA V weapons
(rocket launcher, minigun, pistol), hear GTA V engine sounds and radio. GTA V is a *companion*: all its
content is read at runtime from the player's own install (`{game:gta-v}`); nothing from either game is shipped.
Solo only in v1 (co-op maybe later). Story mode only (online shares the exe).

## Status
- `sheets/` hold the design (source of truth). `python3 -I tools/preflight.py` lists every open cell.
- No plugin code yet and nothing has been run in either game: the build session had no copy of the games
  and could not reach melty.gg (egress policy), so no Melty lookups, recipe validation or upload happened.
- Biggest open risk: GTA V models/sounds/weapons are in GTA V formats; whether they can be converted and
  spawned in RDR2 through the ASI loader alone (no Script Hook RDR2) is unverified (`h_model_convert`,
  `h_spawn_vehicle`, `h_give_weapon`).
