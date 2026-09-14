# 🧠 Corne Keyboard Config - njorquera98

Este repositorio contiene la configuración personalizada del teclado Corne (crkbd) con firmware QMK. Incluye:

* 🔒 Cuatro capas personalizadas (teclas, navegación, símbolos y funciones)
* 📺 Personalización de ambos OLED (ícono de capa + logo animado)
* 🚫 No se utiliza VIA
* 💡 Pensado para facilitar futuras modificaciones

---

## 🧩 Estructura del repositorio

```
corne-zmk-config/
├── keyboards/
│   └── crkbd/
│       ├── crkbd.c
│       ├── info.json
│       ├── keymaps/
│       │   └── njorquera98/
│       │       ├── keymap.c  # Keymap principal
│       │       └── config.h
│       ├── lib/              # Librerías OLED personalizadas
│       ├── r2g/              # Config del lado derecho con OLED
│       └── rev*/             # Archivos de revisión del teclado
```

---

## 🎛 Capas del Teclado

### Layer 0 - Base

```
,-----------------------------------------.               ,-----------------------------------------.
| Tab  |  Q |  W |  E |  R |  T |          |               |          |  Y |  U |  I |  O |  P | Bksp |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
| Ctrl |  A |  S |  D |  F |  G |          |               |          |  H |  J |  K |  L | ;  | '    |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
| Shift|  Z |  X |  C |  V |  B |          |               |          |  N |  M | ,  | .  | /  | Alt  |
`------+------+------+------+------+------'               `------+------+------+------+------+------'
                        | GUI | L1 | Space|               |Enter| L2  | ESC |
                        `------------------'               `------------------'
```

> `Alt` ya está disponible como tecla física fija (esquina inferior derecha, junto a `/`), así que el pulgar `L1` quedó como `MO(1)` simple — nada de tap-hold en la tecla que más se sostiene del teclado. Ver la nota de diseño más abajo.

### Layer 1 - Números, Navegación y gestión de ventanas (Rectangle)

```
,-----------------------------------------.               ,-----------------------------------------------.
| Tab  |  1  |  2  |  3   |  4   |  5   |               |            |  6  |  7  |  8  |  9  |  0  | Bksp |
|------+-----+-----+------+------+------|               |------------+-----+-----+-----+-----+-----+------|
| Ctrl |Home |◧Izq |⬓Abajo|⬒Arriba|◨Der|               |            |Left |Down | Up  |Right|Del  |      |
|------+-----+-----+------+------+------|               |------------+-----+-----+-----+-----+-----+------|
| Shift|End  |⛶Max |⌖Centro|↺Restaur|    |               |            |     |     |     |     |     | GUI  |
`------+-----+-----+------+------+------'               `------------+-----+-----+-----+-----+-----+------'
                        | GUI |TRNS| Space|               |Enter|L3  |RAlt|
                        `------------------'               `------------------'
```

Mano izquierda = atajos de [Rectangle](https://rectangleapp.com) (bindings default: `Ctrl+Opt+Flecha` para mitades, `Ctrl+Opt+Enter` maximizar, `Ctrl+Opt+C` centrar, `Ctrl+Opt+Backspace` restaurar), enviados como una sola tecla vía macros `LCTL(LALT(...))` — no hace falta sostener dos modificadores a la vez. El orden S/D/F/G sigue la misma lectura izquierda→derecha que H/J/K/L en la mano derecha (Izq/Abajo/Arriba/Der), solo que mueve la ventana en vez del cursor. La tecla bajo `B` queda libre (`KC_NO`), reservada para una futura capa/combo de [AeroSpace](https://github.com/nikitabobko/AeroSpace).

### Layer 2 - Símbolos + edición de texto al estilo Mac

```
,-----------------------------------------.               ,-----------------------------------------.
| Tab  |  !  |  @  |  #  |  $  |  %  |     |               |          | ^  | &  | *  | (  | )  | Bksp |
|------+-----+-----+-----+-----+-----|     |               |------+------+------+------+------+------|
| Ctrl |Cmd↑ |Opt← |Opt→ |Cmd← |Cmd→ |     |               |          | -  | =  | [  | ]  | \  | `    |
|------+-----+-----+-----+-----+-----|     |               |------+------+------+------+------+------|
| Shift|Cmd↓ |Opt⌫ |Cmd⌫ |Opt⌦ |     |     |               |          | _  | +  | {  | }  | |  | ~    |
`------+-----+-----+-----+-----+-----'     |               `------+------+------+------+------+------'
                        | GUI |L3  | Space|               |Enter|TRNS|RAlt|
                        `------------------'               `------------------'
```

Mano derecha = símbolos (sin cambios). Mano izquierda = atajos de edición de texto de macOS, enviados como una sola tecla (`LGUI(...)`/`LALT(...)`): `Cmd` solo vive en el pulgar izquierdo, que es el mismo que sostiene `L1` — así que `Cmd+Flecha` es imposible de alcanzar sosteniendo `L1` (mismo pulgar, dos teclas). `L2` en cambio se sostiene con el pulgar **derecho**, dejando la mano izquierda libre para mandar `Cmd+Flecha`/`Opt+Flecha`/`Cmd+⌫`/`Opt+⌫`/`Opt+⌦` de una — nada de sostener dos modificadores. Fila home = navegación (`Cmd+↑/↓` extremos de documento, `Opt+←/→` palabra, `Cmd+←/→` línea); fila inferior = borrado, con la misma progresión de alcance (palabra → línea → palabra hacia adelante). Queda 1 tecla libre (bajo `B`).

### Layer 3 - Funciones / RGB / Multimedia

```
,-----------------------------------------.               ,-----------------------------------------.
|Reset |F1 | F2 | F3 | F4 | F5 |          |               |          |F6 | F7 | F8 | F9 |F10 | F11 |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
|RGB TOG|H+ |S+ |V+ |Bri+|    |           |              |          |Vol+|Play|Prev|    |    |Mute |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
|NEXT |H- |S- |V- |Bri-|    |             |              |         |Vol-|Stop|Next|    |    |      |
`------+------+------+------+------+------'               `------+------+------+------+------+------'
                        | GUI |TRNS| Space|               |Enter|TRNS|RAlt|
                        `------------------'               `------------------'
```

---

## 🧭 Notas de diseño

* **Por qué `L1` no es tap-hold:** se evaluó `LT(1, KC_LALT)` (tap = Option, hold = Layer 1) en el pulgar interno izquierdo, pero es la tecla que más se *sostiene* del mapa (se usa en casi todos los rolls hacia números/flechas/Home/End). Combinar eso con una resolución tap-hold agrega el `TAPPING_TERM` a cada roll y arriesga que una pulsación breve mande `Alt` en vez de activar la capa. Como `Alt` ya vive en una tecla física fija (esquina inferior derecha de Layer 0), no hacía falta duplicarlo ahí — `L1` volvió a ser `MO(1)` simple.
* **Por qué macros y no home-row-mods:** para Rectangle/AeroSpace se evaluó agregar modificadores tap-hold en las letras (home row mods), pero cambia mucho la mecánica de tipeo normal. En cambio, los 8 huecos libres de `_LAYER1` (mano izquierda, home row + bottom row) ahora mandan macros `LCTL(LALT(...))` completas en una sola tecla — se gana el atajo sin tocar la capa base ni sostener combinaciones de 3 teclas.
* **`Cmd` (GUI) y el conflicto con `L1`:** `Cmd` solo existe en el pulgar izquierdo externo, que es el mismo pulgar que sostiene `L1` (donde viven las flechas) — sostener ambos a la vez con un solo pulgar no es posible, así que `Cmd+Flecha` (inicio/fin de línea, muy usado escribiendo texto) quedaba inalcanzable. Se resolvió igual que con Rectangle: `_LAYER2` se sostiene con el pulgar **derecho**, así que su mano izquierda (antes vacía) ahora manda `Cmd`/`Opt` + flecha o borrado como una sola tecla, sin necesitar el pulgar izquierdo para nada. `Cmd+C/V/X/Z` (copiar/pegar/cortar/deshacer) siguen siendo combo de una sola mano (pulgar izq + letra en mano izq) — se evaluó espejar `Cmd` en el pulgar derecho (tap-hold sobre `Esc`) para resolver eso también, pero se dejó pendiente por ahora.
* **Espacio para AeroSpace:** queda 1 tecla libre en `_LAYER1` (bajo `B`) y 1 en `_LAYER2` (bajo `B`) para cuando se configure.

---

## 📺 Personalización del OLED

El keymap define su propio `oled_task_user()` (en [`keymap.c`](keyboards/crkbd/keymaps/njorquera98/keymap.c)):

* **Mitad master (izquierda, USB):** ícono de la capa activa (Base / Nav / Sym / Fn) + etiqueta de texto.
* **Mitad derecha:** logo animado propio, 4 frames por temporizador (sin WPM, no reacciona al tipeo).

Código relacionado:

* [`lib/oled_anim.c`](keyboards/crkbd/lib/oled_anim.c) — bitmaps de íconos + frames de animación y sus renderers.
* [`lib/layer_state_reader.c`](keyboards/crkbd/lib/layer_state_reader.c) — `read_layer_state()` (usa `get_highest_layer()`).
* [`keymaps/njorquera98/tools/gen_oled.py`](keyboards/crkbd/keymaps/njorquera98/tools/gen_oled.py) — genera los bytes de `oled_anim.c` (`python3 gen_oled.py` imprime el `.c`; `--preview` dibuja los bitmaps en ASCII).
* [`r2g.c`](keyboards/crkbd/r2g/r2g.c) — conserva el logo Mechboards R2G como fallback (`weak`).

Los bitmaps (`oled_icon_*`, `oled_anim_frames`) están en formato de página SSD1306, diseñados para `OLED_ROTATION_0`; `crkbd.c` ya rota 180° la mitad no-master.

---

## 📁 Archivos importantes

* `keymap.c`: Keymap principal
* `config.h`: Configuración por capa
* `r2g.c`: Personalización del OLED
* `lib/`: Librerías OLED y capa visual

---

## 🛠 Herramientas útiles

* [QMK Configurator](https://config.qmk.fm)
* [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/)
* [Keymap Editor (JSON)](https://keymap-editor.qmk.fm)

---

## 🚀 Para compilar tu firmware

```bash
qmk compile -kb crkbd/r2g -km njorquera98
```

---

## 📌 Nota

Este proyecto no utiliza VIA por el momento. Se recomienda mantener esta estructura clara para facilitar futuros cambios y debugging.

---

## © 2025 njorquera98

Repositorio de respaldo y documentación del firmware personalizado para teclado Corne con QMK.
