"""_784.py

ConicalPinionMicroGeometryConfig
"""
from mastapy.gears.manufacturing.bevel import _778, _772
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_PINION_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalPinionMicroGeometryConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalPinionMicroGeometryConfig',)


class ConicalPinionMicroGeometryConfig(_772.ConicalGearMicroGeometryConfig):
    """ConicalPinionMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_PINION_MICRO_GEOMETRY_CONFIG

    class _Cast_ConicalPinionMicroGeometryConfig:
        """Special nested class for casting ConicalPinionMicroGeometryConfig to subclasses."""

        def __init__(self, parent: 'ConicalPinionMicroGeometryConfig'):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config(self):
            return self._parent._cast(_772.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _773
            
            return self._parent._cast(_773.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def conical_pinion_micro_geometry_config(self) -> 'ConicalPinionMicroGeometryConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalPinionMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_concave_ob_configuration(self) -> '_778.ConicalMeshFlankNurbsMicroGeometryConfig':
        """ConicalMeshFlankNurbsMicroGeometryConfig: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_convex_ib_configuration(self) -> '_778.ConicalMeshFlankNurbsMicroGeometryConfig':
        """ConicalMeshFlankNurbsMicroGeometryConfig: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConvexIBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig':
        return self._Cast_ConicalPinionMicroGeometryConfig(self)
