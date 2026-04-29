# Add Teams Keybinding

## Context
User wants a Hyprland keybinding to launch Microsoft Teams, which is installed as a PWA.

## Approach
Teams is a PWA, so use `omarchy-launch-or-focus-webapp` (same pattern as WhatsApp, Google Messages, etc.).

Use `SUPER SHIFT, T` for Teams (currently btop). Move btop to `SUPER SHIFT ALT, T`.

## Change
**File:** `~/.config/hypr/bindings.conf`

Replace:
```
bindd = SUPER SHIFT, T, Activity, exec, omarchy-launch-tui btop
```
With:
```
bindd = SUPER SHIFT, T, Teams, exec, omarchy-launch-or-focus-webapp Teams "https://teams.microsoft.com"
bindd = SUPER SHIFT ALT, T, Activity, exec, omarchy-launch-tui btop
```

## Verification
Press `SUPER SHIFT ALT + T` — Teams PWA should open or focus if already running.
