from amaranth.build import *
from amaranth.vendor import XilinxPlatform


__all__ = ["AlchitryPtPlatform"]


class AlchitryPtPlatform(XilinxPlatform):
    device      = "xc7a100t"
    package     = "fgg484"
    speed       = "2"
    default_clk = "clk100"

    resources = [
        Resource("clk100", 0, Pins("N14", dir="i"),
                 Clock(100e6), Attrs(IOSTANDARD="LVCMOS33")),

        # LEDs
        Resource("led", 0, Pins("K13", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 1, Pins("K16", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 2, Pins("L15", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 3, Pins("L14", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 4, Pins("M16", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 5, Pins("M14", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 6, Pins("M12", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 7, Pins("N16", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),

        # Reset button
        Resource("rst_n", 0, Pins("P6", dir="i"), Attrs(IOSTANDARD="LVCMOS33")),

        # IO pins
        Resource("io", 0, Pins("A1", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 1, Pins("A2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 2, Pins("A3", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 3, Pins("A4", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 4, Pins("A5", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 5, Pins("A7", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 6, Pins("A8", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 7, Pins("A9", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 8, Pins("A10", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 9, Pins("A11", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 10, Pins("A13", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 11, Pins("A14", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 12, Pins("A15", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 13, Pins("A16", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 14, Pins("A17", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 15, Pins("A18", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 16, Pins("B1", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 17, Pins("B2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 18, Pins("B4", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 19, Pins("B5", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 20, Pins("B6", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 21, Pins("B7", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 22, Pins("B8", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 23, Pins("B10", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 24, Pins("B11", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 25, Pins("B12", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 26, Pins("B14", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 27, Pins("B15", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 28, Pins("B16", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 29, Pins("B17", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 30, Pins("B18", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 31, Pins("C1", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 32, Pins("C2", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 33, Pins("C4", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 34, Pins("C5", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 35, Pins("C6", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 36, Pins("C7", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 37, Pins("C8", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 38, Pins("C9", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 39, Pins("C10", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 40, Pins("C11", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 41, Pins("C13", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 42, Pins("C14", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 43, Pins("C16", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 44, Pins("C17", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 45, Pins("C18", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 46, Pins("D3", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("io", 47, Pins("D4", dir="io"), Attrs(IOSTANDARD="LVCMOS33")),
    ]

    connectors = []

    def toolchain_program(self, products, name, **kwargs):
        vivado = self.toolchain.sh_command("vivado")
        with products.extract("{}.bit".format(name)) as bitstream_filename:
            self.toolchain.run([
                vivado, "-mode", "batch", "-source", self._create_tcl_script(bitstream_filename)
            ], root="build")

    def _create_tcl_script(self, bitstream_filename):
        tcl_script = "program_fpga.tcl"
        with open(tcl_script, "w") as f:
            f.write(f"""
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
""")
        return tcl_script