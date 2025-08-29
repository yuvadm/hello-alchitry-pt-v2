from amaranth import Elaboratable, Module, Signal, Cat
from amaranth.build import Platform

from platform_alchitry_pt_v2 import AlchitryPtV2Platform


class LEDRunner(Elaboratable):
    def elaborate(self, platform: Platform) -> Module:
        m = Module()

        # Get all 8 LED pins
        leds = [platform.request("led", i) for i in range(8)]
        
        # Create timing counter for LED movement
        counter = Signal(23)  # ~0.084 seconds per step at 100MHz
        
        # Create position counter (0-15 for back-and-forth pattern)
        position = Signal(4)
        direction = Signal()  # 0 = right, 1 = left
        
        # LED pattern register
        led_pattern = Signal(8)
        
        m.d.sync += counter.eq(counter + 1)
        
        # Update position when counter overflows (every ~0.084 seconds at 100MHz)
        with m.If(counter == 0):
            with m.If(direction == 0):  # Moving right
                with m.If(position == 7):
                    m.d.sync += direction.eq(1)  # Change direction
                with m.Else():
                    m.d.sync += position.eq(position + 1)
            with m.Else():  # Moving left
                with m.If(position == 0):
                    m.d.sync += direction.eq(0)  # Change direction
                with m.Else():
                    m.d.sync += position.eq(position - 1)
        
        # Create running LED pattern with trailing effect
        # Use upper bits for dimming trail effect
        trail_on = counter[22]  # Creates 50% duty cycle for trail LEDs
        
        with m.Switch(position):
            for i in range(8):
                with m.Case(i):
                    # Build pattern for this position
                    pattern_bits = []
                    for led_idx in range(8):
                        if led_idx == i:
                            # Main LED always on
                            pattern_bits.append(1)
                        elif led_idx == i-1 and i > 0:
                            # Left trail LED (dimmed)
                            pattern_bits.append(trail_on)
                        elif led_idx == i+1 and i < 7:
                            # Right trail LED (dimmed)
                            pattern_bits.append(trail_on)
                        else:
                            # Other LEDs off
                            pattern_bits.append(0)
                    
                    m.d.comb += led_pattern.eq(Cat(*pattern_bits))
        
        # Connect LED pattern to actual LEDs
        for i, led in enumerate(leds):
            m.d.comb += led.o.eq(led_pattern[i])
        
        return m


if __name__ == "__main__":
    platform = AlchitryPtV2Platform()
    platform.build(LEDRunner(), do_program=True)
