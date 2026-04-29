---
name: Teams LED Notifier Project
description: Building a Teams message notifier that lights up Framework LED Matrix input modules
type: project
---

Working on a Python script that polls Microsoft Teams for unread messages via the Graph API and lights up Framework Laptop 16 LED Matrix input modules.

**Why:** User wants a physical notification when Teams messages arrive.

**How to apply:** Pick up where we left off on this project when the user returns.

## Current Status
- Repo cloned at `/home/vwestberg/Claude/inputmodule-rs`
- udev rules installed: `sudo cp release/50-framework-inputmodule.rules /etc/udev/rules.d/`
- `inputmodule-control` built at: `/home/vwestberg/Claude/inputmodule-rs/target/x86_64-unknown-linux-gnu/release/inputmodule-control`
- Must build with `--target x86_64-unknown-linux-gnu` (workspace default is thumbv6m-none-eabi)
- Two LED Matrix modules detected on `/dev/ttyACM0` and `/dev/ttyACM1`
- LED on: `inputmodule-control led-matrix --pattern all-on`
- LED off: `inputmodule-control led-matrix --sleeping true`

## Next Steps
- User is setting up an Azure AD app registration for Microsoft Graph API access
- Need: Application (client) ID from Azure portal
- Steps given to user:
  1. portal.azure.com > Azure AD > App registrations > New registration
  2. Name: teams-led-notifier
  3. Account types: any org + personal Microsoft accounts
  4. Authentication > Allow public client flows = Yes
  5. API permissions > Microsoft Graph > Delegated > Chat.Read
  6. Copy Application (client) ID
- Plan: Python script using `msal` + Graph API polling chats for unreadMessageCount > 0
- Auth method: device code flow (token cached to ~/.teams_led_token.json)
