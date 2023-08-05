"""_1126.py

AGMA2000A88AccuracyGrader
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1139, _1130
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA2000A88_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'AGMA2000A88AccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMA2000A88AccuracyGrader',)


class AGMA2000A88AccuracyGrader(_1130.CylindricalAccuracyGrader):
    """AGMA2000A88AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _AGMA2000A88_ACCURACY_GRADER

    class _Cast_AGMA2000A88AccuracyGrader:
        """Special nested class for casting AGMA2000A88AccuracyGrader to subclasses."""

        def __init__(self, parent: 'AGMA2000A88AccuracyGrader'):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader(self):
            return self._parent._cast(_1130.CylindricalAccuracyGrader)

        @property
        def agma2000a88_accuracy_grader(self) -> 'AGMA2000A88AccuracyGrader':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMA2000A88AccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_number_of_teeth(self) -> 'float':
        """float: 'AdjustedNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedNumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_pitch_variation(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'AllowablePitchVariation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowablePitchVariation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ProfileTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_runout_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'RadialRunoutTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialRunoutTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_alignment_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ToothAlignmentTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothAlignmentTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def toothto_tooth_composite_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'ToothtoToothCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothtoToothCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_composite_tolerance(self) -> '_1139.OverridableTolerance':
        """OverridableTolerance: 'TotalCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AGMA2000A88AccuracyGrader._Cast_AGMA2000A88AccuracyGrader':
        return self._Cast_AGMA2000A88AccuracyGrader(self)
