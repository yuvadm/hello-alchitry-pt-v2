#!/usr/bin/env python3

from amaranth import *
from amaranth.build import Platform
from platform_alchitry_pt import AlchitryPtPlatform


class Blinky(Elaboratable):
    def elaborate(self, platform: Platform) -> Module:
        m = Module()
        
        # Get the LED pins
        led = platform.request("led", 0)
        
        # Create a counter for timing
        counter = Signal(24)
        
        # Increment counter every clock cycle
        m.d.sync += counter.eq(counter + 1)
        
        # Connect the MSB of counter to LED (blinks at ~12Hz at 100MHz)
        m.d.comb += led.o.eq(counter[-1])
        
        return m


if __name__ == "__main__":
    platform = AlchitryPtPlatform()
    platform.build(Blinky(), do_program=True)