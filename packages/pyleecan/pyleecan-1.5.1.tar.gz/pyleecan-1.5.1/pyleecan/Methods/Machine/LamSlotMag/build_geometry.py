# -*- coding: utf-8 -*-
from numpy import pi

from ....Classes.LamSlot import LamSlot
from ....Classes.SlotM18 import SlotM18
from ....Functions.labels import BOUNDARY_PROP_LAB, MAG_LAB, YSMR_LAB, YSML_LAB


def build_geometry(
    self, is_magnet=True, sym=1, alpha=0, delta=0, is_circular_radius=False
):
    """Build the geometry of the LamSlotMag

    Parameters
    ----------
    self : LamSlotMag
        LamSlotMag object
    is_magnet : bool
        If True build the magnet surfaces
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_circular_radius : bool
        True to add surfaces to "close" the Lamination radii

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """

    st = self.get_label()

    assert (self.slot.Zs % sym) == 0, (
        "ERROR, Wrong symmetry for "
        + st
        + " "
        + str(self.slot.Zs)
        + " slots and sym="
        + str(sym)
    )
    # getting the LamSlot surface
    surf_list = LamSlot.build_geometry(
        self, sym=sym, is_circular_radius=is_circular_radius
    )

    Zs = self.slot.Zs
    slot_pitch = 2 * pi / Zs

    # Add the magnet surface(s)
    if is_magnet and self.magnet is not None:
        mag_surf_list = list()
        # for each magnet to draw
        for ii in range(Zs // sym):
            mag_surf = self.slot.get_surface_active(
                alpha=slot_pitch * ii + slot_pitch * 0.5
            )
            mag_surf_list.append(mag_surf)
            # Adapt the label
            mag_surf_list[-1].label = st + "_" + MAG_LAB + "_R0-T0-S" + str(ii)
        # Update the magnets BC (if magnet side matches sym lines SlotM18 only)
        if isinstance(self.slot, SlotM18) and sym > 1:
            mag_surf_list[0].line_list[0].prop_dict.update(
                {BOUNDARY_PROP_LAB: st + "_" + YSMR_LAB}
            )
            mag_surf_list[-1].line_list[2].prop_dict.update(
                {BOUNDARY_PROP_LAB: st + "_" + YSML_LAB}
            )
        surf_list.extend(mag_surf_list)

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
