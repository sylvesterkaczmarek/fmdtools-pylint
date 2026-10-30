# SPDX-License-Identifier: GPL-3.0-or-later
"""Small static-only model fixture; the typo is intentional."""

from fmdtools.define.block.function import Function
from fmdtools.define.container.state import State


class PumpState(State):
    speed: float = 1.0


class Pump(Function):
    container_s = PumpState

    def read_speed(self):
        return self.s.speeed
