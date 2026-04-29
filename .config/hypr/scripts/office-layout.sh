#!/bin/sh
sleep 1

# Bottom office monitor
hyprctl keyword monitor DP-9,1920x1080@60,0x0,1,transform,0

# Top office monitor (flipped 180°, stacked above)
hyprctl keyword monitor DP-10,1920x1080@60,0x-1080,1,transform,2

# Laptop to the RIGHT, vertically centered between DP-9 and DP-10
hyprctl keyword monitor eDP-1,2560x1600@165,1920x-580,1.6,transform,0

