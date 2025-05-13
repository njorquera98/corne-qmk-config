# 🧠 Corne Keyboard Config - njorquera98

Este repositorio contiene la configuración personalizada del teclado Corne (crkbd) con firmware QMK. Incluye:

* 🔒 Cuatro capas personalizadas (teclas, navegación, símbolos y funciones)
* 📺 Personalización del OLED (lado derecho)
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

En el directorio `keyboards/crkbd/r2g/` se encuentra el código para mostrar una imagen personalizada en el OLED del lado derecho del teclado:

* [`r2g.c`](keyboards/crkbd/r2g/r2g.c)
* [`keyboard.json`](keyboards/crkbd/r2g/keyboard.json)

También se incluye una librería personalizada en `lib/` que gestiona el contenido mostrado: logo, capa activa, RGB, etc.

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
