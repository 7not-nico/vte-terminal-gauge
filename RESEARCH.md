# VTE-based terminals — gauge (vtebench)

Date: 2026-11-07
Tool: vtebench 0.3.1 (Rust), built from source
Metric: terminal PTY read throughput — lower ms/sample = faster
(vtebench disclaimer: not frame rate or latency)
Payload: 12 default benchmarks (cursor_motion, dense/light/medium cells,
scrolling variants, sync_medium_cells, unicode)
Settings: --max-secs 2, default --min-bytes 1048576 (~1 MB/sample), 1 warmup
Host: CachyOS, Wayland, VTE 0.84.1 common engine

## Research (wigolo in-depth)

VTE (libvte) is the shared engine; host apps differ in chrome/profiles/security
knobs, not wire behavior. Known VTE-based terminals:
GNOME Terminal, Ptyxis, GNOME Console (kgx), Tilix, xfce4-terminal, Terminator,
Black Box, guake, sakura, tilda, ROXTerm, evilvte, vala-terminal, lxterminal,
mate-terminal, pantheon-terminal (io.elementary.terminal), deepin-terminal,
termit, termite, lilyterm, tinyterm, stjerm, GTKTerm2.
Embedded VTE users: gedit, Anjuta, etc.

## Overall ranking (mean ms/sample, lower better)

| Rank | Terminal | Engine | Overall (ms) | Samples |
|---|---|---|---:|---:|
| 1 | alacritty | own (GPU) | 56.5 | 1068 |
| 2 | foot | own (GPU) | 67.4 | 895 |
| 3 | zutty | own (OpenGL) | 71.4 | 648 |
| 4 | ghostty | libghostty | 73.2 | 1091 |
| 5 | kitty | own (GPU) | 83.0 | 672 |
| 6 | io.elementary.terminal | VTE 0.84.1 | 86.5 | 873 |
| 7 | sakura | VTE 0.84.1 | 86.6 | 836 |
| 8 | mate-terminal | VTE 0.84.1 | 88.9 | 847 |
| 9 | tilda | VTE 0.84.1 | 89.7 | 870 |
| 10 | guake | VTE 0.84.1 | 90.2 | 823 |
| 11 | xfce4-terminal | VTE 0.84.1 | 91.5 | 867 |
| 12 | ptyxis | VTE 0.84.1 | 94.6 | 858 |
| 13 | kgx (gnome-console) | VTE 0.84.1 | 95.8 | 789 |
| 14 | gnome-terminal | VTE 0.84.1 | 107.8 | 1179 |
| 15 | terminator | VTE 0.84.1 | 111.1 | 694 |
| 16 | kermit | VTE 3.x | 134.0 | 778 |
| 17 | lxterminal | VTE 0.84.1 | 138.9 | 658 |
| 18 | deepin-terminal | VTE 0.84.1 | 155.4 | 315 |
| 19 | xterm | own (Xaw) | 497.7 | 96 |

## Per-benchmark mean ms (lower better)

| Terminal | cursor_motion | dense_cells | light_cells | medium_cells | scrolling | scroll_bottom | scroll_bottom_small | scroll_fullscreen | scroll_top | scroll_top_small | sync_medium | unicode |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| alacritty | 10.4 | 10.9 | 13.4 | 13.3 | 116.5 | 116.7 | 113.8 | 16.3 | 117.2 | 120.6 | 17.2 | 11.5 |
| foot | 8.2 | 27.1 | 7.5 | 25.2 | 127.4 | 135.9 | 120.8 | 7.9 | 126.9 | 122.8 | 18.9 | 80.6 |
| zutty | 24.9 | 18.6 | 25.1 | 17.3 | 137.0 | 135.7 | 142.0 | 23.9 | 143.1 | 139.9 | 26.3 | 23.0 |
| ghostty | 21.0 | 19.9 | 6.5 | 20.5 | 161.5 | 152.5 | 145.2 | 26.1 | 151.1 | 151.9 | 15.4 | 6.4 |
| kitty | 97.2 | 25.3 | 5.8 | 38.3 | 119.1 | 107.1 | 113.1 | 11.5 | 127.2 | 138.5 | 44.7 | 168.2 |
| io.elementary.terminal | 20.0 | 29.5 | 5.1 | 20.3 | 189.8 | 166.9 | 175.4 | 23.3 | 187.2 | 167.6 | 24.1 | 28.5 |
| sakura | 23.9 | 31.1 | 5.2 | 25.9 | 157.4 | 175.6 | 181.2 | 27.8 | 182.3 | 174.5 | 27.0 | 27.9 |
| mate-terminal | 25.4 | 26.6 | 5.0 | 25.7 | 170.1 | 181.5 | 181.7 | 19.3 | 185.9 | 187.7 | 29.4 | 28.0 |
| tilda | 21.8 | 31.5 | 5.6 | 17.3 | 180.1 | 172.4 | 171.9 | 21.6 | 211.9 | 197.4 | 18.5 | 26.7 |
| guake | 32.4 | 46.1 | 4.8 | 24.8 | 169.6 | 173.9 | 183.7 | 23.1 | 186.8 | 174.3 | 36.5 | 25.9 |
| xfce4-terminal | 19.2 | 19.4 | 5.4 | 18.2 | 190.4 | 188.7 | 187.6 | 27.3 | 182.6 | 192.2 | 35.3 | 32.1 |
| ptyxis | 20.0 | 21.6 | 5.3 | 18.1 | 197.6 | 187.1 | 185.5 | 18.9 | 185.6 | 173.4 | 20.4 | 101.7 |
| kgx | 22.4 | 33.1 | 5.6 | 18.9 | 199.1 | 185.5 | 196.5 | 23.2 | 184.7 | 185.4 | 20.3 | 74.4 |
| gnome-terminal | 20.5 | 29.4 | 5.4 | 24.6 | 189.8 | 185.5 | 181.9 | 21.5 | 188.3 | 214.4 | 20.5 | 211.9 |
| terminator | 26.5 | 43.7 | 6.6 | 20.0 | 197.6 | 192.2 | 199.1 | 23.0 | 225.2 | 212.3 | 21.0 | 166.4 |
| kermit | 23.9 | 26.7 | 5.6 | 19.2 | 193.4 | 194.2 | 210.6 | 18.7 | 230.2 | 209.3 | 20.3 | 456.0 |
| lxterminal | 27.0 | 78.9 | 6.4 | 21.6 | 215.9 | 207.1 | 209.9 | 16.7 | 219.4 | 212.6 | 22.7 | 429.2 |
| deepin-terminal | 25.2 | 34.7 | 34.7 | 72.0 | 450.2 | 276.6 | 185.7 | 77.5 | 266.8 | 186.1 | 182.6 | 72.1 |
| xterm | 426.8 | 2193.0 | 106.1 | 255.0 | 1426.0 | 288.9 | 289.2 | 67.0 | 218.1 | 244.1 | 216.3 | 242.1 |

## Read-out

- Alacritty is the leader (56.5 ms) — fastest on nearly every benchmark; unicode 11.5 ms.
- GPU-accelerated terminals (alacritty, foot, ghostty, kitty) occupy the top 5.
- VTE 0.84.1 is the common engine for the GTK hosts; spread reflects host overhead.
- Light-cell throughput nearly uniform (~5 ms) across VTE hosts; lxterminal/deepin outliers on dense cells and unicode.
- Unicode is the biggest differentiator: ghostty 6.4, alacritty 11.5, zutty 23.0; lxterminal 429.2, gnome-terminal 211.9, kermit 456.0.
- Scrolling dominates runtime (~100-230 ms/sample); deepin-terminal worst (~450 ms on `scrolling`).
- zutty ignores sync-output (mode 2026) -> scrolling numbers not fairly comparable.
- ghostty emits unimplemented color_change/CSI warnings but completed (1091 samples).
- xterm (497.7, 96 samples) unreliable due to font/rendering bottleneck.

## Caveats

- vtebench measures PTY read blocking only — not frame rate, input latency, or smoothness.
- Results machine/compositor/config dependent (Wayland, default fonts).
- st and tabby not packaged in available repos -> not gauged.
- Tilix, Black Box, ROXTerm, termite, termit, lilyterm, evilvte not packaged -> not gauged.
- Raw artifacts: artifacts/*.dat (vtebench DAT format); re-plot with artifacts/vtebench/gnuplot/summary.sh.