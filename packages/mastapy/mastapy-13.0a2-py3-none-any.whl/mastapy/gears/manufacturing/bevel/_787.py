"""_787.py

ConicalSetMicroGeometryConfig
"""
from typing import List

from mastapy.gears.manufacturing.bevel import _772, _781, _788
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalSetMicroGeometryConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalSetMicroGeometryConfig',)


class ConicalSetMicroGeometryConfig(_788.ConicalSetMicroGeometryConfigBase):
    """ConicalSetMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MICRO_GEOMETRY_CONFIG

    class _Cast_ConicalSetMicroGeometryConfig:
        """Special nested class for casting ConicalSetMicroGeometryConfig to subclasses."""

        def __init__(self, parent: 'ConicalSetMicroGeometryConfig'):
            self._parent = parent

        @property
        def conical_set_micro_geometry_config_base(self):
            return self._parent._cast(_788.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_implementation_detail(self):
            from mastapy.gears.analysis import _1225
            
            return self._parent._cast(_1225.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def conical_set_micro_geometry_config(self) -> 'ConicalSetMicroGeometryConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalSetMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_micro_geometry_configuration(self) -> 'List[_772.ConicalGearMicroGeometryConfig]':
        """List[ConicalGearMicroGeometryConfig]: 'GearMicroGeometryConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMicroGeometryConfiguration

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes(self) -> 'List[_781.ConicalMeshMicroGeometryConfig]':
        """List[ConicalMeshMicroGeometryConfig]: 'Meshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def duplicate(self) -> 'ConicalSetMicroGeometryConfig':
        """ 'Duplicate' is the original name of this method.

        Returns:
            mastapy.gears.manufacturing.bevel.ConicalSetMicroGeometryConfig
        """

        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'ConicalSetMicroGeometryConfig._Cast_ConicalSetMicroGeometryConfig':
        return self._Cast_ConicalSetMicroGeometryConfig(self)
