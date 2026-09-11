#include <stdio.h>
#include "action_layer.h"

// This keymap activates its layers in a nested way (MO(3) is pressed from
// inside layer 1 or layer 2), so layer_state can hold a *sum* of bits
// (e.g. 0b1010 = 10) that never matches a fixed bitmask.  Use the highest
// active layer instead and map it to the four real layers of the keymap.

char layer_state_str[24];

const char *read_layer_state(void) {
  switch (get_highest_layer(layer_state)) {
    case 0:
      snprintf(layer_state_str, sizeof(layer_state_str), "Layer: Base");
      break;
    case 1:
      snprintf(layer_state_str, sizeof(layer_state_str), "Layer: Nav");
      break;
    case 2:
      snprintf(layer_state_str, sizeof(layer_state_str), "Layer: Sym");
      break;
    case 3:
      snprintf(layer_state_str, sizeof(layer_state_str), "Layer: Fn");
      break;
    default:
      snprintf(layer_state_str, sizeof(layer_state_str), "Layer: %d", get_highest_layer(layer_state));
  }

  return layer_state_str;
}
