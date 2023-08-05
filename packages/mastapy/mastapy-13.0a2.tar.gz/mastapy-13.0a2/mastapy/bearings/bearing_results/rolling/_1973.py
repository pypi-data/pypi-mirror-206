"""_1973.py

LoadedAsymmetricSphericalRollerBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _2013
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAsymmetricSphericalRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAsymmetricSphericalRollerBearingElement',)


class LoadedAsymmetricSphericalRollerBearingElement(_2013.LoadedRollerBearingElement):
    """LoadedAsymmetricSphericalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedAsymmetricSphericalRollerBearingElement:
        """Special nested class for casting LoadedAsymmetricSphericalRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedAsymmetricSphericalRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(self):
            return self._parent._cast(_2013.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_asymmetric_spherical_roller_bearing_element(self) -> 'LoadedAsymmetricSphericalRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAsymmetricSphericalRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedAsymmetricSphericalRollerBearingElement._Cast_LoadedAsymmetricSphericalRollerBearingElement':
        return self._Cast_LoadedAsymmetricSphericalRollerBearingElement(self)
