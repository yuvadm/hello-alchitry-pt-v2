# Hello Alchitry Pt v2

A basic Amaranth HDL blinky example for the Alchitry Pt v2 development board with XC7A100T-2FGG484I FPGA.

## Requirements

- Python 3.12+
- uv package manager
- Xilinx Vivado 2025.1 (installed at `~/Xilinx/2025.1/Vivado/`)
- Alchitry Pt v2 board connected via USB

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Set up Vivado environment (add to your shell profile):
```bash
export PATH="$HOME/Xilinx/2025.1/Vivado/bin:$PATH"
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
from platform_alchitry_pt import AlchitryPtPlatform
from blinky import Blinky
platform = AlchitryPtPlatform()
platform.build(Blinky(), do_program=False)
"
```

### Manual Programming

If you need to program manually after building:
```bash
cd build
vivado -mode batch -source program_fpga.tcl
```

## Files

- `blinky.py` - Main blinky example that blinks LED 0
- `platform_alchitry_pt.py` - Alchitry Pt v2 platform definition with pin mappings
- `pyproject.toml` - Project dependencies (Amaranth HDL)

## Hardware Details

- **FPGA**: XC7A100T-2FGG484I (Artix-7, 484-pin BGA, speed grade -2)
- **Clock**: 100 MHz oscillator on pin N14
- **LEDs**: 8 LEDs (pins K13, K16, L15, L14, M16, M14, M12, N16)
- **Reset**: Active-low reset button on pin P6
- **IO**: 48 general purpose IO pins available

The example uses a 24-bit counter clocked at 100 MHz, with the MSB driving LED 0 for a blink rate of approximately 12 Hz.
