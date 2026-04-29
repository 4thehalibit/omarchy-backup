# Omarchy Config Backup

Backup of customized config files from my Omarchy (Hyprland-based Arch Linux) desktop setup.

Created before migrating to NixOS — use this to restore configs if switching back to Omarchy.

## What's included

| Config | Description |
|--------|-------------|
| `.config/hypr/` | Hyprland, Hypridle, Hyprlock configs + scripts |
| `.config/waybar/` | Floating waybar config, styles, and custom scripts |
| `.config/omarchy/` | Omarchy branding (L&S Electric screensaver), themes |
| `.config/mako/` | Notification daemon config |
| `.config/walker/` | App launcher config |
| `.config/ghostty/` | Ghostty terminal config |
| `.config/kitty/` | Kitty terminal config |
| `.config/alacritty/` | Alacritty terminal config |
| `.config/starship.toml` | Shell prompt config |

## Notable customizations

- **Screensaver**: L&S Electric ASCII art (`omarchy/branding/screensaver.txt`)
- **Hyprlock**: Large clock, date, weather via wttr.in, rounded input field
- **Hypridle**: Screensaver timeout set to 10 minutes
- **Waybar**: Floating pill-style bar, CPU/battery/volume values, calendar widget
- **Calendar widget**: `waybar/scripts/cal-widget.py` — weather + 2 months side by side, today highlighted

## Restoring to Omarchy

Copy configs back to `~/.config/`:

```bash
cp -r .config/* ~/.config/
```

Then restart Waybar:

```bash
omarchy-restart-waybar
```

Hyprland configs reload automatically on next login or via `hyprctl reload`.
