from ....Functions.labels import WEDGE_LAB


def get_surface_wedges(self, alpha=0, delta=0):
    """Return the list of surfaces defining the wedges area of the Slot

    Parameters
    ----------
    self : Slot
        A Slot object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list : list
        list of surfaces objects
    """

    if self.wedge_mat is None:
        return []  # No wedges
    else:
        # By default Wedge is the full opening surface
        surf_list = self.get_surface_opening()
        if self.parent is not None:
            # Adapt label
            lam_lab = self.parent.get_label()
            for surf in surf_list:
                surf.label = lam_lab + "_" + WEDGE_LAB + "_R0-T0-S0"

        # Apply transformation
        for surf in surf_list:
            surf.rotate(alpha)
            surf.translate(delta)

        return surf_list
