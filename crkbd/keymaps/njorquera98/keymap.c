#include QMK_KEYBOARD_H


#define _LAYER0 0
#define _LAYER1 1
#define _LAYER2 2
#define _LAYER3 3

enum custom_keycodes {
    LAYER0 = SAFE_RANGE,
    LAYER1,
    LAYER2,
    LAYER3,
};

// macOS Rectangle shortcuts (default bindings), sent as one keypress instead
// of holding Ctrl+Opt yourself. Live on _LAYER1's left hand, mirroring the
// arrow cluster already on the right hand (S/D/F/G = same left-to-right
// order as H/J/K/L, just "move the window" instead of "move the cursor").
#define RECT_LEFT    LCTL(LALT(KC_LEFT))   // Left half
#define RECT_DOWN    LCTL(LALT(KC_DOWN))   // Bottom half
#define RECT_UP      LCTL(LALT(KC_UP))     // Top half
#define RECT_RIGHT   LCTL(LALT(KC_RGHT))   // Right half
#define RECT_MAX     LCTL(LALT(KC_ENT))    // Maximize
#define RECT_CENTER  LCTL(LALT(KC_C))      // Center
#define RECT_RESTORE LCTL(LALT(KC_BSPC))   // Restore / undo last resize

 const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

 [_LAYER0] = LAYOUT(KC_TAB, KC_Q, KC_W, KC_E, KC_R, KC_T, KC_Y, KC_U, KC_I, KC_O, KC_P, KC_BSPC, KC_LCTL, KC_A, KC_S, KC_D, KC_F, KC_G, KC_H, KC_J, KC_K, KC_L, KC_SCLN, KC_QUOT, KC_LSFT, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_N, KC_M, KC_COMM, KC_DOT, KC_SLSH, KC_LALT, KC_LGUI, MO(1), KC_SPC, KC_ENT, MO(2), KC_ESC),

[_LAYER1] = LAYOUT(KC_TAB, KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7, KC_8, KC_9, KC_0, KC_BSPC, KC_LCTL, KC_HOME, RECT_LEFT, RECT_DOWN, RECT_UP, RECT_RIGHT, KC_LEFT, KC_DOWN, KC_UP, KC_RGHT, KC_NO, KC_DEL, KC_LSFT, KC_END, RECT_MAX, RECT_CENTER, RECT_RESTORE, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_LGUI, KC_TRNS, KC_SPC, KC_ENT, MO(3), KC_RALT),

[_LAYER2] = LAYOUT(KC_TAB, KC_EXLM, KC_AT, KC_HASH, KC_DLR, KC_PERC, KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, KC_BSPC, KC_LCTL, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_MINS, KC_EQL, KC_LBRC, KC_RBRC, KC_BSLS, KC_GRV, KC_LSFT, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO, KC_UNDS, KC_PLUS, KC_LCBR, KC_RCBR, KC_PIPE, KC_TILD, KC_LGUI, MO(3), KC_SPC, KC_ENT, KC_TRNS, KC_RALT),

[_LAYER3] = LAYOUT(QK_BOOT, KC_F1, KC_F2, KC_F3, KC_F4, KC_F5, KC_F6, KC_F7, KC_F8, KC_F9, KC_F10, KC_F11, RM_TOGG, RM_HUEU, RM_SATU, RM_VALU, KC_BRIU, KC_NO, KC_VOLU, KC_MPLY, KC_MPRV, KC_NO, KC_NO, KC_MUTE, RM_NEXT, RM_HUED, RM_SATD, RM_VALD, KC_BRID, KC_NO, KC_VOLD, KC_MSTP, KC_MNXT, KC_NO, KC_NO, KC_NO, KC_LGUI, KC_TRNS, KC_SPC, KC_ENT, KC_TRNS, KC_RALT)

};

#ifdef OLED_ENABLE
// Defined in keyboards/crkbd/lib/oled_anim.c (added via rules.mk)
void oled_render_layer_state(void);
void oled_render_anim(void);

// Master half shows the current layer (icon + label); the other half runs the
// timer-driven logo animation.  Returning false stops crkbd.c from also drawing
// its default layer/keylog/logo screens.
bool oled_task_user(void) {
    if (is_keyboard_master()) {
        oled_render_layer_state();
    } else {
        oled_render_anim();
    }
    return false;
}
#endif
