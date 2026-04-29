---
name: Omarchy Desktop Customization / Eiros Migration
description: Customizations from Omarchy (Arch/Hyprland) setup, now migrating to Eiros (NixOS) — https://github.com/lcleveland/eiros
type: project
originSessionId: 1fb5e404-604d-4a2b-baf1-3beb42a67371
---
Migrating from Omarchy (Hyprland-based Arch Linux) to **Eiros** (NixOS flake config by lcleveland).
Eiros uses MangoWC compositor + Dank Material Shell instead of Hyprland/Waybar.
Configs backed up to `~/omarchy-backup/` for reference when re-implementing customizations in Nix.

**Why:** Switching to NixOS for declarative, reproducible system config.

**Changes made so far:**

- `~/.config/hypr/hypridle.conf` — screensaver timeout changed to 10min (was 2.5min)
- `~/.config/omarchy/branding/screensaver.txt` — replaced Omarchy logo with "L&S Electric" ASCII art (slant font for L/Electric/S, big font for &)
- `~/.config/hypr/hyprlock.conf` — added large clock, date, weather (wttr.in auto-detect), rounded input field, animations enabled
- `~/.config/waybar/config.jsonc` — floating bar (margin 8px), height 36px, CPU/battery/volume show values, calendar module added
- `~/.config/waybar/style.css` — floating rounded bar, pill-style module backgrounds, workspace styling
- `~/.config/waybar/scripts/cal-widget.py` — custom calendar widget: weather + 2 months side by side with box-drawing borders, today highlighted in red

**How to apply:** Run `omarchy-restart-waybar` after waybar changes. Hyprland configs auto-reload.

**Notes:**
- Weather uses wttr.in auto IP detection — detects Antigo WI instead of Merrill WI (ISP routing quirk, weather data is still accurate)
- figlet is installed for ASCII art generation
- User works at L&S Electric and travels frequently
