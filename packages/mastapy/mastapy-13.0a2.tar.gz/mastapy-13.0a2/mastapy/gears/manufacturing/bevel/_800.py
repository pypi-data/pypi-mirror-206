"""_800.py

PinionConvex
"""
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _818
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _801
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_CONVEX = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionConvex')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionConvex',)


class PinionConvex(_0.APIBase):
    """PinionConvex

    This is a mastapy class.
    """

    TYPE = _PINION_CONVEX

    class _Cast_PinionConvex:
        """Special nested class for casting PinionConvex to subclasses."""

        def __init__(self, parent: 'PinionConvex'):
            self._parent = parent

        @property
        def pinion_convex(self) -> 'PinionConvex':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionConvex.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_convex_ib_configuration(self) -> '_818.BasicConicalGearMachineSettingsGenerated':
        """BasicConicalGearMachineSettingsGenerated: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConvexIBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex(self) -> '_801.PinionFinishMachineSettings':
        """PinionFinishMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PinionConvex._Cast_PinionConvex':
        return self._Cast_PinionConvex(self)
