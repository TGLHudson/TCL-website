# Style guide: Hudson family of sites

These colours, fonts and component styles are taken from the live **hudsonglobalconsulting.com** (Hudson Global Consulting, HGC), read from its computed styles on 2 November 2026. Use them for all three sites so they read as one family:

- **HGC**: hudsonglobalconsulting.com (the parent brand)
- **Hudson Risk Culture (HRC)**: hudsonriskculture.com
- **The Culture Ladder (TCL)**: thecultureladder.com

Each site keeps its own name and content, but uses the same palette, type and components. Any departure from this file needs Tim's agreement first.

## Colour palette

| Token | Hex | Where HGC uses it |
|---|---|---|
| `--ink` | `#000718` | Page background (near-black navy) |
| `--deep-teal` | `#003E4A` | Large section and panel backgrounds |
| `--deep-teal-2` | `#003E4E` | Section eyebrow headings, button borders (see contrast note) |
| `--teal` | `#349699` | Accent panels, highlights |
| `--gold` | `#F4E59B` | Key headings (h2), button text |
| `--gold-muted` | `#E8DD93` | Links, navigation call to action |
| `--cream` | `#F9EECA` | Thin divider rules (1px) |
| `--text` | `#E8E6E6` | Body text and h1/h3 on dark backgrounds |
| `--ink-text` | `#0A0A1C` | Text on light backgrounds, where used |

```css
:root {
  --ink: #000718;
  --deep-teal: #003E4A;
  --deep-teal-2: #003E4E;
  --teal: #349699;
  --gold: #F4E59B;
  --gold-muted: #E8DD93;
  --cream: #F9EECA;
  --text: #E8E6E6;
  --ink-text: #0A0A1C;
}
```

The scheme is dark: light text on a near-black navy, with gold for emphasis and teal for structure. It is not a light site with dark accents.

### Contrast warning: fix this, do not copy it

On HGC, the eyebrow headings ("INDUSTRIES WE SERVE", "WHAT WE CAN DELIVER") and the button borders use `#003E4E` on the `#000718` background. That is roughly 1.7:1 contrast, which fails the Web Content Accessibility Guidelines (WCAG); AA needs 4.5:1 for normal text and 3:1 for large text and interface parts. On the new sites, use `--teal` (`#349699`, about 5.8:1) for eyebrows and button borders. Keep `--deep-teal` and `--deep-teal-2` for backgrounds only.

## Typography

| Role | Font | Weight | Size | Notes |
|---|---|---|---|---|
| Headings h1 to h4 | Montserrat | 600 | h1 48px, h2 40px, h3 32px, h4 24px | Line height about 1.3; sentence case |
| Section eyebrow | Montserrat | 600 | 24px (HGC); 14 to 16px reads better | Uppercase, `--teal` |
| Body | Source Sans 3 (formerly Source Sans Pro) | 400 | 17px | Line height about 1.85; `--text` |
| Buttons | Montserrat | 600 | 13px | Uppercase, letter-spacing 1px |

- Load both fonts from Google Fonts, or self-host them for privacy and speed (preferred), with a system sans-serif as fallback.
- HGC's hero h1 is in Roboto. That looks like a leftover. Use Montserrat for every heading on the new sites.

## Components

**Buttons (primary call to action).** Outline style: transparent background, 2px solid border in `--teal`, text in `--gold`, square corners (`border-radius: 0`), padding 10px 20px, Montserrat 600 13px uppercase, letter-spacing 1px. On hover, fill with `--deep-teal`.

**Links.** `--gold-muted`, no underline at rest, underlined on hover and focus. Focus states must always be visible.

**Dividers.** 1px solid `--cream` rules between list items, as in HGC's "What we can deliver" list, with a right-pointing arrow (→) on each row.

**Hero.** Full-bleed dark photograph under a navy overlay, left-aligned text: an uppercase eyebrow with wide letter-spacing, the h1 in `--text`, a short list of credentials, then one outline button. Where no suitable photograph exists, leave a marked placeholder.

**Tiles.** Image tiles with a dark overlay and the label in large, bold, white uppercase, as in HGC's "Industries we serve". Square corners.

**Corners and depth.** Square corners throughout. No drop shadows, no rounded cards, no gradients beyond photographic overlays.

## Layout

- Content width: about 1100 to 1200px maximum, centred, with generous vertical spacing between sections.
- Two-column sections: heading and call to action on the left, list on the right.
- Mobile first. Tiles and two-column sections stack on small screens.

## Per-site accent (proposal: confirm with Tim)

To tell the three sites apart while keeping them one family:
- HGC: gold leads (as now).
- HRC: teal leads, gold as secondary.
- TCL: gold leads; the book cover sets any additional colour once CRC Press supplies it.
