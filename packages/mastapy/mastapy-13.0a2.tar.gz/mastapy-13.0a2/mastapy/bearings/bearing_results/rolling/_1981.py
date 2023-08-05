"""_1981.py

LoadedAxialThrustNeedleRollerBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _1978
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAxialThrustNeedleRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAxialThrustNeedleRollerBearingElement',)


class LoadedAxialThrustNeedleRollerBearingElement(_1978.LoadedAxialThrustCylindricalRollerBearingElement):
    """LoadedAxialThrustNeedleRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedAxialThrustNeedleRollerBearingElement:
        """Special nested class for casting LoadedAxialThrustNeedleRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedAxialThrustNeedleRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(self):
            return self._parent._cast(_1978.LoadedAxialThrustCylindricalRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(self):
            from mastapy.bearings.bearing_results.rolling import _2012
            
            return self._parent._cast(_2012.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2013
            
            return self._parent._cast(_2013.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(self) -> 'LoadedAxialThrustNeedleRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAxialThrustNeedleRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedAxialThrustNeedleRollerBearingElement._Cast_LoadedAxialThrustNeedleRollerBearingElement':
        return self._Cast_LoadedAxialThrustNeedleRollerBearingElement(self)
