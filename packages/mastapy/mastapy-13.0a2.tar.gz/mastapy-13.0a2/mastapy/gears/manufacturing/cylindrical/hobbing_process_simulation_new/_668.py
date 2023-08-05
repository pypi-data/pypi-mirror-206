"""_668.py

HobbingProcessSimulationNew
"""
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _662, _663, _664, _665,
    _666, _670, _681, _667
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessSimulationNew')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessSimulationNew',)


class HobbingProcessSimulationNew(_681.ProcessSimulationNew['_667.HobbingProcessSimulationInput']):
    """HobbingProcessSimulationNew

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_SIMULATION_NEW

    class _Cast_HobbingProcessSimulationNew:
        """Special nested class for casting HobbingProcessSimulationNew to subclasses."""

        def __init__(self, parent: 'HobbingProcessSimulationNew'):
            self._parent = parent

        @property
        def process_simulation_new(self):
            return self._parent._cast(_681.ProcessSimulationNew)

        @property
        def hobbing_process_simulation_new(self) -> 'HobbingProcessSimulationNew':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hobbing_process_gear_shape_calculation(self) -> '_662.HobbingProcessGearShape':
        """HobbingProcessGearShape: 'HobbingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessGearShapeCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_lead_calculation(self) -> '_663.HobbingProcessLeadCalculation':
        """HobbingProcessLeadCalculation: 'HobbingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessLeadCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_mark_on_shaft_calculation(self) -> '_664.HobbingProcessMarkOnShaft':
        """HobbingProcessMarkOnShaft: 'HobbingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessMarkOnShaftCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_pitch_calculation(self) -> '_665.HobbingProcessPitchCalculation':
        """HobbingProcessPitchCalculation: 'HobbingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessPitchCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_profile_calculation(self) -> '_666.HobbingProcessProfileCalculation':
        """HobbingProcessProfileCalculation: 'HobbingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessProfileCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_total_modification(self) -> '_670.HobbingProcessTotalModificationCalculation':
        """HobbingProcessTotalModificationCalculation: 'HobbingProcessTotalModification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessTotalModification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HobbingProcessSimulationNew._Cast_HobbingProcessSimulationNew':
        return self._Cast_HobbingProcessSimulationNew(self)
