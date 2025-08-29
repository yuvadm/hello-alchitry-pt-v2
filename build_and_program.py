#!/usr/bin/env python3

import os
import sys

# Add Vivado to PATH
vivado_bin = os.path.expanduser("~/Xilinx/2025.1/Vivado/bin")
os.environ["PATH"] = vivado_bin + ":" + os.environ.get("PATH", "")

# Now run the original blinky script
from blinky import Blinky
from platform_alchitry_pt import AlchitryPtPlatform

if __name__ == "__main__":
    platform = AlchitryPtPlatform()
    platform.build(Blinky(), do_program=True)