from amaranth.build import *
from amaranth.vendor import XilinxPlatform


__all__ = ["AlchitryPtPlatform"]


class AlchitryPtPlatform(XilinxPlatform):
    device      = "xc7a100t"
    package     = "fgg484"
    speed       = "2"
    default_clk = "clk100"

    resources = [
        # 100MHz clock - using official pin from Alchitry Labs
        Resource("clk100", 0, Pins("W19", dir="i"),
                 Clock(100e6), Attrs(IOSTANDARD="LVCMOS33")),

        # LEDs - official pins from Alchitry Labs
        Resource("led", 0, Pins("P19", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 1, Pins("P20", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 2, Pins("T21", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 3, Pins("R19", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 4, Pins("V22", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 5, Pins("U21", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 6, Pins("T20", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 7, Pins("W20", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),

        # Reset button - official pin from Alchitry Labs  
        Resource("rst_n", 0, Pins("N15", dir="i"), Attrs(IOSTANDARD="LVCMOS33")),

        # A-Bank IO pins - official pins from Alchitry Labs (subset for convenience)
        Resource("io", 0, Pins("AB22", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # A3
        Resource("io", 1, Pins("AB21", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # A5
        Resource("io", 2, Pins("E3", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),    # A9
        Resource("io", 3, Pins("F3", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),    # A11
        Resource("io", 4, Pins("M2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),    # A15
        Resource("io", 5, Pins("M3", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),    # A17
        Resource("io", 6, Pins("J6", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),    # A21
        Resource("io", 7, Pins("K6", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),    # A23
        Resource("io", 8, Pins("AB18", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # A4
        Resource("io", 9, Pins("AA18", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # A6
        Resource("io", 10, Pins("N2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # A10
        Resource("io", 11, Pins("P2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # A12
        Resource("io", 12, Pins("L1", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # A16
        Resource("io", 13, Pins("M1", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # A18
        Resource("io", 14, Pins("D2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # A22
        Resource("io", 15, Pins("E2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # A24

        # B-Bank IO pins - official pins from Alchitry Labs (subset)
        Resource("io", 16, Pins("AB13", dir="io"), Attrs(IOSTANDARD="LVCMOS33")), # B3
        Resource("io", 17, Pins("AA13", dir="io"), Attrs(IOSTANDARD="LVCMOS33")), # B5
        Resource("io", 18, Pins("AB12", dir="io"), Attrs(IOSTANDARD="LVCMOS33")), # B9
        Resource("io", 19, Pins("AB11", dir="io"), Attrs(IOSTANDARD="LVCMOS33")), # B11
        Resource("io", 20, Pins("AA11", dir="io"), Attrs(IOSTANDARD="LVCMOS33")), # B4
        Resource("io", 21, Pins("AA10", dir="io"), Attrs(IOSTANDARD="LVCMOS33")), # B6
        Resource("io", 22, Pins("Y14", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # B10
        Resource("io", 23, Pins("W14", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # B12

        # C-Bank IO pins - official pins from Alchitry Labs
        Resource("io", 24, Pins("U18", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # C29
        Resource("io", 25, Pins("U17", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # C31
        Resource("io", 26, Pins("V2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # C33
        Resource("io", 27, Pins("U2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # C35
        Resource("io", 28, Pins("Y1", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # C30
        Resource("io", 29, Pins("W1", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),   # C32
        Resource("io", 30, Pins("R14", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # C34
        Resource("io", 31, Pins("P14", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),  # C36
    ]

    connectors = []

    def toolchain_program(self, products, name, **kwargs):
        import subprocess
        import os
        
        with products.extract("{}.bit".format(name)) as bitstream_filename:
            # Create TCL script for programming
            tcl_content = f"""
open_hw_manager
connect_hw_server
open_hw_target
set_property PROGRAM.FILE {{{bitstream_filename}}} [get_hw_devices xc7a100t_0]
set_property PROBES.FILE {{}} [get_hw_devices xc7a100t_0]
set_property FULL_PROBES.FILE {{}} [get_hw_devices xc7a100t_0]
current_hw_device [get_hw_devices xc7a100t_0]
program_hw_devices [get_hw_devices xc7a100t_0]
close_hw_manager
exit
"""
            tcl_script = "program_fpga.tcl"
            tcl_full_path = os.path.join("build", tcl_script)
            with open(tcl_full_path, "w") as f:
                f.write(tcl_content)
            
            # Run vivado to program the FPGA
            subprocess.run(["vivado", "-mode", "batch", "-source", tcl_script], 
                         cwd="build", check=True)