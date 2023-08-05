"""_483.py

VDI2737SafetyFactorReportingObject
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VDI2737_SAFETY_FACTOR_REPORTING_OBJECT = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'VDI2737SafetyFactorReportingObject')


__docformat__ = 'restructuredtext en'
__all__ = ('VDI2737SafetyFactorReportingObject',)


class VDI2737SafetyFactorReportingObject(_0.APIBase):
    """VDI2737SafetyFactorReportingObject

    This is a mastapy class.
    """

    TYPE = _VDI2737_SAFETY_FACTOR_REPORTING_OBJECT

    class _Cast_VDI2737SafetyFactorReportingObject:
        """Special nested class for casting VDI2737SafetyFactorReportingObject to subclasses."""

        def __init__(self, parent: 'VDI2737SafetyFactorReportingObject'):
            self._parent = parent

        @property
        def vdi2737_safety_factor_reporting_object(self) -> 'VDI2737SafetyFactorReportingObject':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VDI2737SafetyFactorReportingObject.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crack_initiation(self) -> 'float':
        """float: 'CrackInitiation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrackInitiation

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_fracture(self) -> 'float':
        """float: 'FatigueFracture' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueFracture

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_deformation(self) -> 'float':
        """float: 'PermanentDeformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentDeformation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'VDI2737SafetyFactorReportingObject._Cast_VDI2737SafetyFactorReportingObject':
        return self._Cast_VDI2737SafetyFactorReportingObject(self)
