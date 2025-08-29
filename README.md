# Hello Alchitry Pt V2

A basic Amaranth HDL blinky example for the Alchitry Pt V2 development board with XC7A100T-2FGG484I FPGA.

## Requirements

- Python 3.13+
- uv package manager
- Xilinx Vivado (with `vivado` command in PATH)
- Alchitry Pt V2 board connected via USB

## Setup

1. **Install Python dependencies:**
   ```bash
   uv sync
   ```

2. **Install udev rules for USB access:**
   ```bash
   sudo cp 99-alchitry-xilinx.rules /etc/udev/rules.d/
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

3. **Ensure Vivado is in PATH:**
   ```bash
   export PATH="/path/to/vivado/bin:$PATH"
   ```

## Usage

### Build and Program FPGA

Run the blinky example:
```bash
uv run python blinky.py
```

This will:
1. Synthesize the design using Vivado
2. Generate a bitstream
3. Program the FPGA automatically
4. LED 0 should start blinking at ~12Hz

### Build Only (No Programming)

To build without programming:
```bash
uv run python -c "
from platform_alchitry_pt_v2 import AlchitryPtV2Platform
from blinky import Blinky
platform = AlchitryPtV2Platform()
platform.build(Blinky(), do_program=False)
"
```

## Files

- `blinky.py` - Main blinky example that blinks LED 0
- `platform_alchitry_pt_v2.py` - Alchitry Pt V2 platform definition with official pin mappings
- `pyproject.toml` - Project dependencies
- `99-alchitry-xilinx.rules` - udev rules for USB programming access

## Hardware Details

- **FPGA**: XC7A100T-2FGG484I (Artix-7, 484-pin BGA, speed grade -2)
- **Clock**: 100 MHz oscillator on pin W19
- **LEDs**: 8 LEDs (pins P19, P20, T21, R19, V22, U21, T20, W20)
- **Reset**: Active-low reset button on pin N15
- **IO**: 32 general purpose IO pins from A/B/C banks

Pin mappings are sourced from official Alchitry Labs V2 hardware definitions.
