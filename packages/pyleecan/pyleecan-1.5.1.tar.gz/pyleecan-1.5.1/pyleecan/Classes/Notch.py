# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Notch.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Notch
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.Notch.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from ..Methods.Machine.Notch.get_Ryoke import get_Ryoke
except ImportError as error:
    get_Ryoke = error

try:
    from ..Methods.Machine.Notch.is_outwards import is_outwards
except ImportError as error:
    is_outwards = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Notch(FrozenClass):
    """Abstract class for notches"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Notch.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Machine.Notch.get_Ryoke
    if isinstance(get_Ryoke, ImportError):
        get_Ryoke = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method get_Ryoke: " + str(get_Ryoke))
            )
        )
    else:
        get_Ryoke = get_Ryoke
    # cf Methods.Machine.Notch.is_outwards
    if isinstance(is_outwards, ImportError):
        is_outwards = property(
            fget=lambda x: raise_(
                ImportError("Can't use Notch method is_outwards: " + str(is_outwards))
            )
        )
    else:
        is_outwards = is_outwards
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            assert "__class__" in init_dict
            assert init_dict["__class__"] == "Notch"
        if init_str is not None:  # Initialisation by str
            assert type(init_str) is str
        # The class is frozen, for now it's impossible to add new properties
        self.parent = None
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Notch_str = ""
        if self.parent is None:
            Notch_str += "parent = None " + linesep
        else:
            Notch_str += "parent = " + str(type(self.parent)) + " object" + linesep
        return Notch_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        Notch_dict = dict()
        # The class name is added to the dict for deserialisation purpose
        Notch_dict["__class__"] = "Notch"
        return Notch_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)()
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""
        pass
