"""_2133.py

CrossedRollerBearing
"""
from mastapy.bearings.bearing_designs.rolling import _2147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'CrossedRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('CrossedRollerBearing',)


class CrossedRollerBearing(_2147.RollerBearing):
    """CrossedRollerBearing

    This is a mastapy class.
    """

    TYPE = _CROSSED_ROLLER_BEARING

    class _Cast_CrossedRollerBearing:
        """Special nested class for casting CrossedRollerBearing to subclasses."""

        def __init__(self, parent: 'CrossedRollerBearing'):
            self._parent = parent

        @property
        def roller_bearing(self):
            return self._parent._cast(_2147.RollerBearing)

        @property
        def rolling_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2150
            
            return self._parent._cast(_2150.RollingBearing)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2116
            
            return self._parent._cast(_2116.DetailedBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2119
            
            return self._parent._cast(_2119.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2115
            
            return self._parent._cast(_2115.BearingDesign)

        @property
        def crossed_roller_bearing(self) -> 'CrossedRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CrossedRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CrossedRollerBearing._Cast_CrossedRollerBearing':
        return self._Cast_CrossedRollerBearing(self)
