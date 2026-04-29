

#!/bin/sh
sleep 1

# HOME HDMI — 4K scaled display
hyprctl keyword monitor "desc:ViewSonic Corporation VX3211-4K",3840x2160@60,0x0,1.5,transform,0

# Laptop to the RIGHT of HDMI (use LOGICAL width: 3840 / 1.5 = 2560)
hyprctl keyword monitor eDP-1,2560x1600@165,2560x0,1.6,transform,0

