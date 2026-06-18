"""WeAct 4.2" 400x300 panel (SSD1683) driven in MONOCHROME mode.

The panel is physically 3-color (black/white/red), but here we ignore the red
plane so we can use the controller's fast B/W partial refresh (~1-2s) via the
EPaperMono driver. Use `full_update_every: N` to do a clean full refresh every
N-th update and clear the ghosting that partial updates accumulate.
"""

from . import EpaperModel


class WeActMono(EpaperModel):
    """WeAct B/W/R 4.2" panel forced to monochrome for fast partial refresh."""

    def __init__(self, name, **defaults):
        super().__init__(name, "EPaperMono", **defaults)

    def get_init_sequence(self, config):
        _, height = self.get_dimensions(config)
        h1 = height - 1
        return (
            (0x01, h1 & 0xFF, h1 >> 8, 0x00),  # Driver output control (gate lines)
            (0x11, 0x03),                      # Data entry mode: X+, Y+
            (0x3C, 0x05),                      # Border waveform
            (0x18, 0x80),                      # Internal temperature sensor
            (0x21, 0x00, 0x80),                # Display update control 1
        )


# Model: WeAct 4.2" 400x300 (SSD1683) in monochrome / fast-partial mode
weact_4p2_mono = WeActMono(
    "weact-4.2in-mono",
    width=400,
    height=300,
    data_rate="10MHz",
    minimum_update_interval="1s",
)
