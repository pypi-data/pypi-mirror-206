"""_1133.py

CylindricalGearAccuracyTolerances
"""
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
    _1126, _1127, _1129, _1135,
    _1136
)
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ACCURACY_TOLERANCES = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'CylindricalGearAccuracyTolerances')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearAccuracyTolerances',)


class CylindricalGearAccuracyTolerances(_0.APIBase):
    """CylindricalGearAccuracyTolerances

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ACCURACY_TOLERANCES

    class _Cast_CylindricalGearAccuracyTolerances:
        """Special nested class for casting CylindricalGearAccuracyTolerances to subclasses."""

        def __init__(self, parent: 'CylindricalGearAccuracyTolerances'):
            self._parent = parent

        @property
        def cylindrical_gear_accuracy_tolerances(self) -> 'CylindricalGearAccuracyTolerances':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearAccuracyTolerances.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def agma2000_gear_accuracy_tolerances(self) -> '_1126.AGMA2000A88AccuracyGrader':
        """AGMA2000A88AccuracyGrader: 'AGMA2000GearAccuracyTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AGMA2000GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def agma2015_gear_accuracy_tolerances(self) -> '_1127.AGMA20151A01AccuracyGrader':
        """AGMA20151A01AccuracyGrader: 'AGMA2015GearAccuracyTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AGMA2015GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def agmaiso13281_gear_accuracy_tolerances(self) -> '_1129.AGMAISO13281B14AccuracyGrader':
        """AGMAISO13281B14AccuracyGrader: 'AGMAISO13281GearAccuracyTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AGMAISO13281GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso132811995_gear_accuracy_tolerances(self) -> '_1135.ISO132811995AccuracyGrader':
        """ISO132811995AccuracyGrader: 'ISO132811995GearAccuracyTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO132811995GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso132812013_gear_accuracy_tolerances(self) -> '_1136.ISO132812013AccuracyGrader':
        """ISO132812013AccuracyGrader: 'ISO132812013GearAccuracyTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO132812013GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearAccuracyTolerances._Cast_CylindricalGearAccuracyTolerances':
        return self._Cast_CylindricalGearAccuracyTolerances(self)
