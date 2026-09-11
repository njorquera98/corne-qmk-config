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

### Layer 2 - Símbolos

```
,-----------------------------------------.               ,-----------------------------------------.
| Tab  | !  | @  | #  | $  | %  |          |               |          | ^  | &  | *  | (  | )  | Bksp |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
| Ctrl |    |    |    |    |    |          |               |          | -  | =  | [  | ]  | \  | `    |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
| Shift|    |    |    |    |    |          |               |          | _  | +  | {  | }  | |  | ~    |
`------+------+------+------+------+------'               `------+------+------+------+------+------'
                        | GUI |L3  | Space|               |Enter|TRNS|RAlt|
                        `------------------'               `------------------'
```

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
* **Espacio para AeroSpace:** queda 1 tecla libre en `_LAYER1` (bajo `B`) y toda `_LAYER2`/mano izquierda sigue con `KC_NO` disponibles para cuando se configure.

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
