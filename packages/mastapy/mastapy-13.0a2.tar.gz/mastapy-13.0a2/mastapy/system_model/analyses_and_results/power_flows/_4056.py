"""_4056.py

CylindricalGearGeometricEntityDrawStyle
"""
from mastapy.system_model.analyses_and_results.power_flows import _4098
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_GEOMETRIC_ENTITY_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CylindricalGearGeometricEntityDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearGeometricEntityDrawStyle',)


class CylindricalGearGeometricEntityDrawStyle(_4098.PowerFlowDrawStyle):
    """CylindricalGearGeometricEntityDrawStyle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_GEOMETRIC_ENTITY_DRAW_STYLE

    class _Cast_CylindricalGearGeometricEntityDrawStyle:
        """Special nested class for casting CylindricalGearGeometricEntityDrawStyle to subclasses."""

        def __init__(self, parent: 'CylindricalGearGeometricEntityDrawStyle'):
            self._parent = parent

        @property
        def power_flow_draw_style(self):
            return self._parent._cast(_4098.PowerFlowDrawStyle)

        @property
        def draw_style(self):
            from mastapy.geometry import _303
            
            return self._parent._cast(_303.DrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _304
            
            return self._parent._cast(_304.DrawStyleBase)

        @property
        def cylindrical_gear_geometric_entity_draw_style(self) -> 'CylindricalGearGeometricEntityDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearGeometricEntityDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle':
        return self._Cast_CylindricalGearGeometricEntityDrawStyle(self)
