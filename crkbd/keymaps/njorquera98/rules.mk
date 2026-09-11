OLED_ENABLE = yes

# Custom OLED code lives in keyboards/crkbd/lib/
SRC += lib/layer_state_reader.c
SRC += lib/oled_anim.c

# The animation is timer driven, so WPM tracking is intentionally NOT enabled.
