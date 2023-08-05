"""_798.py

PinionConcave
"""
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _818
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _801
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_CONCAVE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionConcave')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionConcave',)


class PinionConcave(_0.APIBase):
    """PinionConcave

    This is a mastapy class.
    """

    TYPE = _PINION_CONCAVE

    class _Cast_PinionConcave:
        """Special nested class for casting PinionConcave to subclasses."""

        def __init__(self, parent: 'PinionConcave'):
            self._parent = parent

        @property
        def pinion_concave(self) -> 'PinionConcave':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PinionConcave.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_concave_ob_configuration(self) -> '_818.BasicConicalGearMachineSettingsGenerated':
        """BasicConicalGearMachineSettingsGenerated: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave(self) -> '_801.PinionFinishMachineSettings':
        """PinionFinishMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PinionConcave._Cast_PinionConcave':
        return self._Cast_PinionConcave(self)
