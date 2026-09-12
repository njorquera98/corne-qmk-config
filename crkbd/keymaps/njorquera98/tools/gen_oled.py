#!/usr/bin/env python3
"""Generate QMK OLED raw bitmaps (SSD1306 page format, rotation 0 authoring).

Output byte order matches oled_write_raw_P at rotation 0/180:
  index = page * WIDTH + x , bit (y % 8) with LSB = topmost row of the page.
"""

W = 128


class Grid:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.px = [[0] * w for _ in range(h)]

    def set(self, x, y, v=1):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[y][x] = v

    def rect(self, x0, y0, x1, y1, fill=False):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if fill or x in (x0, x1) or y in (y0, y1):
                    self.set(x, y)

    def hline(self, x0, x1, y):
        for x in range(x0, x1 + 1):
            self.set(x, y)

    def vline(self, x, y0, y1):
        for y in range(y0, y1 + 1):
            self.set(x, y)

    def disc(self, cx, cy, r, fill=True, thick=1):
        for y in range(cy - r - 1, cy + r + 2):
            for x in range(cx - r - 1, cx + r + 2):
                d2 = (x - cx) ** 2 + (y - cy) ** 2
                if fill:
                    if d2 <= r * r:
                        self.set(x, y)
                else:
                    if (r - thick) ** 2 <= d2 <= r * r:
                        self.set(x, y)

    def tri(self, pts):
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        for y in range(min(ys), max(ys) + 1):
            for x in range(min(xs), max(xs) + 1):
                if self._in_tri((x, y), pts):
                    self.set(x, y)

    @staticmethod
    def _sign(a, b, c):
        return (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])

    def _in_tri(self, p, t):
        d1 = self._sign(p, t[0], t[1])
        d2 = self._sign(p, t[1], t[2])
        d3 = self._sign(p, t[2], t[0])
        neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        return not (neg and pos)

    def bytes(self):
        pages = self.h // 8
        out = []
        for page in range(pages):
            for x in range(self.w):
                b = 0
                for bit in range(8):
                    if self.px[page * 8 + bit][x]:
                        b |= (1 << bit)
                out.append(b)
        return out


def emit(name, data, per_line=16):
    lines = [f"const char PROGMEM {name}[] = {{"]
    for i in range(0, len(data), per_line):
        chunk = ", ".join(f"0x{b:02x}" for b in data[i:i + per_line])
        lines.append(f"    {chunk},")
    lines.append("};")
    return "\n".join(lines)


# ---------------------------------------------------------------- layer icons
# 128 x 24  (3 pages).  Motif centred; label text is drawn separately by
# oled_write() so the icon band stays purely graphical.

def icon_base():
    g = Grid(W, 24)
    # a little row of six keycaps = "the base keymap"
    kw, kh, gap = 14, 16, 4
    total = 6 * kw + 5 * gap
    x = (W - total) // 2
    for _ in range(6):
        g.rect(x, 4, x + kw - 1, 4 + kh - 1)
        g.rect(x + 3, 7, x + kw - 4, 4 + kh - 4)  # inner dish
        x += kw + gap
    return g.bytes()


def icon_nav():
    g = Grid(W, 24)
    cx, cy = W // 2, 12
    # four arrows around a hub -> navigation layer
    g.rect(cx - 3, cy - 3, cx + 3, cy + 3)
    g.tri([(cx - 2, cy - 6), (cx + 2, cy - 6), (cx, cy - 11)])          # up
    g.tri([(cx - 2, cy + 6), (cx + 2, cy + 6), (cx, cy + 11)])          # down
    g.tri([(cx - 6, cy - 2), (cx - 6, cy + 2), (cx - 11, cy)])          # left
    g.tri([(cx + 6, cy - 2), (cx + 6, cy + 2), (cx + 11, cy)])          # right
    # long guide bars left/right
    g.hline(6, cx - 18, cy)
    g.hline(cx + 18, W - 7, cy)
    return g.bytes()


def icon_sym():
    g = Grid(W, 24)
    cx = W // 2
    # big  { }  with  [ ]  nested  -> symbol layer
    # left brace
    bx = cx - 26
    g.vline(bx, 4, 19)
    g.hline(bx, bx + 4, 4)
    g.hline(bx, bx + 4, 19)
    g.hline(bx - 4, bx, 11)
    g.set(bx - 5, 12)
    g.hline(bx - 4, bx, 13)
    # right brace (mirror)
    rx = cx + 26
    g.vline(rx, 4, 19)
    g.hline(rx - 4, rx, 4)
    g.hline(rx - 4, rx, 19)
    g.hline(rx, rx + 4, 11)
    g.set(rx + 5, 12)
    g.hline(rx, rx + 4, 13)
    # centre brackets
    g.rect(cx - 12, 7, cx - 4, 16)
    g.rect(cx + 4, 7, cx + 12, 16)
    # centre dots (like ... / operator)
    for dx in (-2, 0, 2):
        g.set(cx + dx, 12)
    return g.bytes()


def icon_fn():
    g = Grid(W, 24)
    cx, cy = W // 2, 11
    # gear = function / settings / media layer
    # eight teeth around the rim
    import math
    for k in range(8):
        a = k * math.pi / 4
        tx = cx + int(round(10 * math.cos(a)))
        ty = cy + int(round(10 * math.sin(a)))
        g.rect(tx - 1, ty - 1, tx + 1, ty + 1, fill=True)
    g.disc(cx, cy, 8, fill=False, thick=3)
    g.disc(cx, cy, 2, fill=True)
    # "Fn" wordmark to the left
    g.vline(12, cy - 6, cy + 6)
    g.hline(12, 19, cy - 6)
    g.hline(12, 17, cy)
    g.vline(24, cy - 3, cy + 6)
    g.vline(30, cy - 3, cy + 6)
    g.hline(25, 29, cy - 3)
    # play triangle to the right -> media keys also live on this layer
    g.tri([(W - 22, cy - 6), (W - 22, cy + 6), (W - 12, cy)])
    return g.bytes()


# ---------------------------------------------------------------- animation
# 128 x 32 (4 pages), 3 frames (kept to 3 - not 4 - to leave enough flash for
# the rest of the keymap on the atmega32u4). Original little "signal bot": a
# rounded head with two eyes that blinks, bobbing over a scrolling wave.
# Timer driven.
ANIM_FRAMES = 3

def wave(g, phase, y0):
    import math
    for x in range(0, W):
        y = y0 + int(round(2.5 * math.sin((x / 9.0) + phase)))
        g.set(x, y)
        g.set(x, y + 1)


def anim_frame(i):
    g = Grid(W, 32)
    bob = [0, -1, 0][i]
    cx = W // 2
    cy = 12 + bob
    # head
    g.rect(cx - 16, cy - 9, cx + 16, cy + 9)
    g.set(cx - 16, cy - 9, 0); g.set(cx + 16, cy - 9, 0)
    g.set(cx - 16, cy + 9, 0); g.set(cx + 16, cy + 9, 0)
    # antenna
    g.vline(cx, cy - 14, cy - 10)
    g.disc(cx, cy - 15, 2, fill=True)
    # eyes: open on frames 0,1 ; blink (closed) on frame 2
    if i == 2:
        g.hline(cx - 11, cx - 4, cy)
        g.hline(cx + 4, cx + 11, cy)
    else:
        look = [-1, 1][i]
        g.disc(cx - 7 + look, cy, 3, fill=True)
        g.disc(cx + 7 + look, cy, 3, fill=True)
    # mouth
    g.hline(cx - 6, cx + 6, cy + 6)
    # scrolling wave along the bottom
    wave(g, phase=i * 1.4, y0=27)
    return g.bytes()


def main():
    parts = []
    parts.append("// Generated by keymaps/njorquera98/tools/gen_oled.py - edit the generator.")
    parts.append("// SSD1306 page format, authored for OLED rotation 0 (driver flips the")
    parts.append("// off-hand half by 180 on its own).")
    parts.append("")
    parts.append('#include "progmem.h"')
    parts.append("")
    parts.append(emit("oled_icon_base", icon_base()))
    parts.append("")
    parts.append(emit("oled_icon_nav", icon_nav()))
    parts.append("")
    parts.append(emit("oled_icon_sym", icon_sym()))
    parts.append("")
    parts.append(emit("oled_icon_fn", icon_fn()))
    parts.append("")
    frames = [anim_frame(i) for i in range(ANIM_FRAMES)]
    body = [f"const char PROGMEM oled_anim_frames[{ANIM_FRAMES}][512] = {{"]
    for fr in frames:
        body.append("    {")
        for j in range(0, len(fr), 16):
            chunk = ", ".join(f"0x{b:02x}" for b in fr[j:j + 16])
            body.append(f"        {chunk},")
        body.append("    },")
    body.append("};")
    parts.append("\n".join(body))
    parts.append("")
    print("\n".join(parts))


def preview():
    import sys

    def show(title, data, h):
        print(f"\n=== {title} ({W}x{h}) ===", file=sys.stderr)
        pages = h // 8
        rows = [[" "] * W for _ in range(h)]
        for page in range(pages):
            for x in range(W):
                b = data[page * W + x]
                for bit in range(8):
                    if b & (1 << bit):
                        rows[page * 8 + bit][x] = "#"
        for r in rows:
            print("".join(r), file=sys.stderr)

    show("BASE", icon_base(), 24)
    show("NAV", icon_nav(), 24)
    show("SYM", icon_sym(), 24)
    show("FN", icon_fn(), 24)
    for i in range(ANIM_FRAMES):
        show(f"ANIM {i}", anim_frame(i), 32)


if __name__ == "__main__":
    import sys
    if "--preview" in sys.argv:
        preview()
    else:
        main()
