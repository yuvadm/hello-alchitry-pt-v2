from amaranth.build import Resource, Pins, Attrs, Clock, DiffPairs
from amaranth.vendor import XilinxPlatform


__all__ = ["AlchitryPtV2Platform"]


# Based on pinouts published by Alchitry Labs, latest commit 7a6bd06d133ee2033c34f2e89a751889329da12b
# https://github.com/alchitry/Alchitry-Labs-V2/blob/master/src/main/kotlin/com/alchitry/labs2/hardware/pinout/PtV2AlphaTopPin.kt
# https://github.com/alchitry/Alchitry-Labs-V2/blob/master/src/main/kotlin/com/alchitry/labs2/hardware/pinout/PtV2BottomPin.kt
# https://github.com/alchitry/Alchitry-Labs-V2/blob/master/src/main/kotlin/com/alchitry/labs2/hardware/pinout/PtV2TopPin.kt


class AlchitryPtV2Platform(XilinxPlatform):
    device = "xc7a100t"
    package = "fgg484"
    speed = "2"
    default_clk = "clk100"

    resources = [
        # 100MHz clock - official pin from Alchitry Labs
        Resource(
            "clk100",
            0,
            Pins("W19", dir="i"),
            Clock(100e6),
            Attrs(IOSTANDARD="LVCMOS33"),
        ),
        # Reset button - official pin from Alchitry Labs
        Resource("rst_n", 0, Pins("N15", dir="i"), Attrs(IOSTANDARD="LVCMOS33")),
        # LEDs - official pins from Alchitry Labs
        Resource("led", 0, Pins("P19", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 1, Pins("P20", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 2, Pins("T21", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 3, Pins("R19", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 4, Pins("V22", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 5, Pins("U21", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 6, Pins("T20", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("led", 7, Pins("W20", dir="o"), Attrs(IOSTANDARD="LVCMOS33")),
    ]

    # Helper function to add a range of IO resources
    def _add_io_resources(self, prefix, start_idx, pins_dict, io_standard="LVCMOS33"):
        for name, fpga_pin in pins_dict.items():
            # Adjust index for sequential numbering starting from start_idx
            # We assume 'A3', 'A4', 'A5', etc., implies an underlying sequential numbering
            # If the original labels are important, you might use them as sub-identifiers
            # For simplicity, I'm assigning sequential indices based on iteration order.
            # You might want to map 'A3' to index 3 if that's preferred.
            self.resources.append(
                Resource(
                    "io_{}{}".format(prefix, name.lower()),
                    0,  # Index 0 since we're using the full name as unique identifier
                    Pins(fpga_pin, dir="io"),
                    Attrs(IOSTANDARD=io_standard),
                )
            )

    def __init__(self):
        super().__init__()

        # --- Top Side Pins (PtV2AlphaTopPin and PtV2TopPin are identical for these banks) ---
        # A Bank Pins (Top Side)
        top_a_pins = {
            "A3": "AB22",
            "A5": "AB21",
            "A9": "E3",
            "A11": "F3",
            "A15": "M2",
            "A17": "M3",
            "A21": "J6",
            "A23": "K6",
            "A27": "M5",
            "A29": "M6",
            "A33": "P4",
            "A35": "P5",
            "A39": "G4",
            "A41": "H4",
            "A45": "J4",
            "A47": "K4",
            "A51": "P1",
            "A53": "R1",
            "A57": "B2",
            "A59": "C2",
            "A63": "F1",
            "A65": "G1",
            "A69": "H5",
            "A71": "J5",
            "A75": "J1",
            "A77": "K1",
            "A4": "AB18",
            "A6": "AA18",
            "A10": "N2",
            "A12": "P2",
            "A16": "L1",
            "A18": "M1",
            "A22": "D2",
            "A24": "E2",
            "A28": "L4",
            "A30": "L5",
            "A34": "N5",
            "A36": "P6",
            "A40": "G3",
            "A42": "H3",
            "A46": "K3",
            "A48": "L3",
            "A52": "N3",
            "A54": "N4",
            "A58": "A1",
            "A60": "B1",
            "A64": "D1",
            "A66": "E1",
            "A70": "G2",
            "A72": "H2",
            "A76": "J2",
            "A78": "K2",
        }
        for i, (name, pin) in enumerate(top_a_pins.items()):
            self.resources.append(
                Resource(
                    "io_top_a", i, Pins(pin, dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                )
            )

        # B Bank Pins (PtV2AlphaTopPin vs PtV2TopPin has differences here)
        # Using PtV2TopPin for consistency with the example and it seems more generic for V2
        top_b_pins = {
            "B3": "R14",
            "B5": "P14",
            "B9": "R17",
            "B11": "P16",
            "B15": "W17",
            "B17": "V17",
            "B21": "AB20",
            "B23": "AA19",
            "B27": "Y19",
            "B29": "Y18",
            "B33": "AB10",
            "B35": "AA9",
            "B39": "W12",
            "B41": "W11",
            "B45": "V14",
            "B47": "V13",
            "B51": "W10",
            "B53": "V10",
            "B57": "AB12",
            "B59": "AB11",
            "B63": "AA11",
            "B65": "AA10",
            "B69": "AB13",
            "B71": "AA13",
            "B75": "AA14",
            "B77": "Y13",
            "B4": "R16",
            "B6": "P15",
            "B10": "P17",
            "B12": "N17",
            "B16": "T18",
            "B18": "R18",
            "B22": "V19",
            "B24": "V18",
            "B28": "V20",
            "B30": "U20",
            "B34": "AB15",
            "B36": "AA15",
            "B40": "Y12",
            "B42": "Y11",
            "B46": "V15",
            "B48": "U15",
            "B52": "AB17",
            "B54": "AB16",
            "B58": "AA16",
            "B60": "Y16",
            "B64": "T15",
            "B66": "T14",
            "B70": "Y14",
            "B72": "W14",
            "B76": "W16",
            "B78": "W15",
        }
        for i, (name, pin) in enumerate(top_b_pins.items()):
            self.resources.append(
                Resource(
                    "io_top_b", i, Pins(pin, dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                )
            )

        # C Bank Pins (Top Side)
        top_c_pins = {
            "C29": "U18",
            "C31": "U17",
            "C33": "V2",
            "C35": "U2",
            "C30": "Y1",
            "C32": "W1",
            "C34": "N14",
            "C36": "N13",
        }
        for i, (name, pin) in enumerate(top_c_pins.items()):
            self.resources.append(
                Resource(
                    "io_top_c", i, Pins(pin, dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                )
            )

        # --- Bottom Side Pins (PtV2BottomPin) ---
        # A Bank Pins (Bottom Side)
        bottom_a_pins = {
            "A3": "AB1",
            "A5": "AA1",
            "A9": "D16",
            "A11": "E16",
            "A15": "A19",
            "A17": "A18",
            "A21": "C20",
            "A23": "D20",
            "A27": "B22",
            "A29": "C22",
            "A33": "B13",
            "A35": "C13",
            "A39": "C17",
            "A41": "D17",
            "A45": "C19",
            "A47": "C18",
            "A51": "F14",
            "A53": "F13",
            "A57": "E17",
            "A59": "F16",
            "A63": "E18",
            "A65": "F18",
            "A69": "G22",
            "A71": "G21",
            "A75": "D15",
            "A77": "D14",
            "A4": "AA3",
            "A6": "Y3",
            "A10": "A16",
            "A12": "A15",
            "A16": "A21",
            "A18": "B21",
            "A22": "D21",
            "A24": "E21",
            "A28": "D22",
            "A30": "E22",
            "A34": "A14",
            "A36": "A13",
            "A40": "B18",
            "A42": "B17",
            "A46": "D19",
            "A48": "E19",
            "A52": "B16",
            "A54": "B15",
            "A58": "F20",
            "A60": "F19",
            "A64": "A20",
            "A66": "B20",
            "A70": "C15",
            "A72": "C14",
            "A76": "E14",
            "A78": "E13",
        }
        for i, (name, pin) in enumerate(bottom_a_pins.items()):
            self.resources.append(
                Resource(
                    "io_bottom_a", i, Pins(pin, dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                )
            )

        # B Bank Pins (Bottom Side)
        bottom_b_pins = {
            "B3": "Y2",
            "B5": "W2",
            "B9": "Y7",
            "B11": "Y8",
            "B15": "AA6",
            "B17": "Y6",
            "B21": "AB2",
            "B23": "AB3",
            "B27": "T6",
            "B29": "R6",
            "B33": "V8",
            "B35": "V9",
            "B39": "W4",
            "B41": "V4",
            "B45": "T4",
            "B47": "R4",
            "B51": "E10",
            "B53": "F10",
            "B57": "C7",
            "B59": "D7",
            "B63": "A6",
            "B65": "B6",
            "B69": "C5",
            "B71": "D5",
            "B75": "A4",
            "B77": "B4",
            "B4": "AB6",
            "B6": "AB7",
            "B10": "AB8",
            "B12": "AA8",
            "B16": "AB5",
            "B18": "AA5",
            "B22": "Y9",
            "B24": "W9",
            "B28": "W7",
            "B30": "V7",
            "B34": "V5",
            "B36": "U6",
            "B40": "AA4",
            "B42": "Y4",
            "B46": "U5",
            "B48": "T5",
            "B52": "E6",
            "B54": "F6",
            "B58": "C11",
            "B60": "D11",
            "B64": "A10",
            "B66": "B10",
            "B70": "C9",
            "B72": "D9",
            "B76": "A8",
            "B78": "B8",
        }
        for i, (name, pin) in enumerate(bottom_b_pins.items()):
            self.resources.append(
                Resource(
                    "io_bottom_b", i, Pins(pin, dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                )
            )

        # C Bank Pins (Bottom Side)
        bottom_c_pins = {
            "C29": "U1",
            "C31": "T1",
            "C33": "R2",
            "C35": "R3",
            "C30": "W5",
            "C32": "W6",
            "C34": "V3",
            "C36": "U3",
        }
        for i, (name, pin) in enumerate(bottom_c_pins.items()):
            self.resources.append(
                Resource(
                    "io_bottom_c", i, Pins(pin, dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                )
            )

        # --- Dedicated Peripherals (from PtV2TopPin as it contains more) ---

        # USB Controller
        self.resources.extend(
            [
                Resource(
                    "usb_rx", 0, Pins("AA20", dir="i"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_tx", 0, Pins("AA21", dir="o"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_d", 2, Pins("W21", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_d", 3, Pins("W22", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_d", 4, Pins("Y21", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_d", 5, Pins("Y22", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_d", 6, Pins("F15", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_d", 7, Pins("U7", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_rxf", 0, Pins("F21", dir="i"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_txe", 0, Pins("T3", dir="i"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_rd", 0, Pins("T16", dir="o"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_wr", 0, Pins("U16", dir="o"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "usb_siwui", 0, Pins("Y17", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
            ]
        )

        # SPI Flash
        self.resources.extend(
            [
                Resource(
                    "spi_d", 0, Pins("P22", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "spi_d", 1, Pins("R22", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "spi_d", 2, Pins("P21", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "spi_d", 3, Pins("R21", dir="io"), Attrs(IOSTANDARD="LVCMOS33")
                ),
                Resource(
                    "spi_sck", 0, Pins("L12", dir="o"), Attrs(IOSTANDARD="LVCMOS33")
                ),  # Bank 0, but usually has special IOSTANDARD
                Resource(
                    "spi_ss", 0, Pins("T19", dir="o"), Attrs(IOSTANDARD="LVCMOS33")
                ),
            ]
        )

        # DDR3 SDRAM - These generally require specific IO standards (SSTL135 for DDR3)
        # Note: Pin types (DQ, DQS, DM, A, BA, etc.) are crucial for memory interfaces.
        # Amaranth's build system supports complex memory resource definitions.
        # This is a simplified representation. For full DDR functionality, you'd
        # likely use a dedicated memory controller in your design.
        ddr_attrs = Attrs(
            IOSTANDARD="SSTL135_R",
            SLEW="FAST",  # Commonly used for DDR IO
            DIFF_TERM="TRUE",
        )  # Differential termination for DQS
        ddr_ck_attrs = Attrs(
            IOSTANDARD="DIFF_SSTL135_R", DIFF_TERM="TRUE"
        )  # Differential clock
        ddr_ctrl_attrs = Attrs(IOSTANDARD="SSTL135_R", SLEW="FAST")

        # Data Group 0
        for i in range(8):
            self.resources.append(
                Resource(
                    "ddr_dq",
                    i,
                    Pins(f"DDR_DQ{i}", dir="io", conn=("ddr", 0)),
                    ddr_attrs,
                )
            )
        self.resources.extend(
            [
                Resource("ddr_dqs", 0, DiffPairs("K21", "K22", dir="io"), ddr_attrs),
                Resource("ddr_dm", 0, Pins("H22", dir="o"), ddr_attrs),
            ]
        )

        # Data Group 1
        for i in range(8, 16):
            self.resources.append(
                Resource(
                    "ddr_dq",
                    i,
                    Pins(f"DDR_DQ{i}", dir="io", conn=("ddr", 1)),
                    ddr_attrs,
                )
            )
        self.resources.extend(
            [
                Resource("ddr_dqs", 1, DiffPairs("J14", "H14", dir="io"), ddr_attrs),
                Resource("ddr_dm", 1, Pins("G13", dir="o"), ddr_attrs),
            ]
        )

        # Control and Address
        self.resources.extend(
            [
                Resource("ddr_odt", 0, Pins("M17", dir="o"), ddr_ctrl_attrs),
                Resource(
                    "ddr_reset_n", 0, Pins("J19", dir="o"), ddr_ctrl_attrs
                ),  # Active low reset
                Resource("ddr_ba", 0, Pins("K19", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_ba", 1, Pins("N20", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_ba", 2, Pins("M20", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_ck", 0, DiffPairs("K17", "J17", dir="o"), ddr_ck_attrs),
                Resource("ddr_cke", 0, Pins("M22", dir="o"), ddr_ctrl_attrs),
                Resource(
                    "ddr_cs_n", 0, Pins("N19", dir="o"), ddr_ctrl_attrs
                ),  # Active low chip select
                Resource(
                    "ddr_ras_n", 0, Pins("L20", dir="o"), ddr_ctrl_attrs
                ),  # Active low RAS
                Resource(
                    "ddr_cas_n", 0, Pins("N22", dir="o"), ddr_ctrl_attrs
                ),  # Active low CAS
                Resource(
                    "ddr_we_n", 0, Pins("L19", dir="o"), ddr_ctrl_attrs
                ),  # Active low WE
                Resource("ddr_a", 0, Pins("K14", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 1, Pins("M15", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 2, Pins("N18", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 3, Pins("K16", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 4, Pins("L14", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 5, Pins("K18", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 6, Pins("M13", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 7, Pins("L18", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 8, Pins("L13", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 9, Pins("M18", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 10, Pins("K13", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 11, Pins("L15", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 12, Pins("M16", dir="o"), ddr_ctrl_attrs),
                Resource("ddr_a", 13, Pins("L16", dir="o"), ddr_ctrl_attrs),
            ]
        )

        # Analog Pins (usually 0V/1.35V reference, not standard digital IO)
        self.resources.extend(
            [
                Resource("vp", 0, Pins("L10", dir="i")),  # Voltage Positive Reference
                Resource("vn", 0, Pins("M9", dir="i")),  # Voltage Negative Reference
            ]
        )

        # Connectors for general purpose IO
        # These are now effectively covered by the _add_io_resources calls,
        # but you might want explicit connector definitions if you use them
        # in a structured way (e.g., "Pmod connector 0", "Header J1")
        # For now, the individually named io_top_a, io_bottom_b, etc., are more granular.
        self.connectors = []  # Keeping it empty as granular definitions are better

    def toolchain_program(self, products, name, **kwargs):
        import subprocess
        import os

        with products.extract("{}.bit".format(name)) as bitstream_filename:
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

            subprocess.run(
                ["vivado", "-mode", "batch", "-source", tcl_script],
                cwd="build",
                check=True,
            )
