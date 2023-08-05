"""_806.py

Wheel
"""
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _816
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.cutters import _810
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WHEEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'Wheel')


__docformat__ = 'restructuredtext en'
__all__ = ('Wheel',)


class Wheel(_0.APIBase):
    """Wheel

    This is a mastapy class.
    """

    TYPE = _WHEEL

    class _Cast_Wheel:
        """Special nested class for casting Wheel to subclasses."""

        def __init__(self, parent: 'Wheel'):
            self._parent = parent

        @property
        def wheel(self) -> 'Wheel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Wheel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_conical_gear_machine_settings(self) -> '_816.BasicConicalGearMachineSettings':
        """BasicConicalGearMachineSettings: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicConicalGearMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_finish_cutter(self) -> '_810.WheelFinishCutter':
        """WheelFinishCutter: 'WheelFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelFinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Wheel._Cast_Wheel':
        return self._Cast_Wheel(self)
