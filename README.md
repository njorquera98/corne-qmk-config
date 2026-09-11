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
                        | GUI |L1/Alt| Space|              |Enter| L2  | ESC |
                        `------------------'               `------------------'
```

> El pulgar izquierdo interno es `LT(1, KC_LALT)`: *tap* = Option (Alt izq), *hold* = Layer 1.

### Layer 1 - Números y Navegación

```
,-----------------------------------------.               ,-----------------------------------------.
| Tab  |  1 |  2 |  3 |  4 |  5 |          |               |          |  6 |  7 |  8 |  9 |  0 | Bksp |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
| Ctrl |Home|    |    |    |    |          |               |          |Left|Down| Up |Right|Del |     |
|------+------+------+------+------+------|               |------+------+------+------+------+------|
| Shift|End |    |    |    |    |          |               |          |    |    |    |    |    | GUI  |
`------+------+------+------+------+------'               `------+------+------+------+------+------'
                        | GUI |TRNS| Space|               |Enter|L3  |RAlt|
                        `------------------'               `------------------'
```

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
