# -*- coding: utf-8 -*-

from numpy import arcsin, cos, pi, sin


def comp_surface_opening(self):
    """Compute the Slot opening surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    S: float
        Slot opening surface [m**2]

    """

    Rbo = self.get_Rbo()
    point_dict = self._comp_point_coordinate()
    Z7 = point_dict["Z7"]
    W1 = abs(Z7.imag) * 2

    S1 = (W1 + self.W0) * self.H1 / 2
    S0 = self.W0 * self.H0

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    if self.is_outwards():
        return S1 + S0 - Sarc
    else:
        return S1 + S0 + Sarc
