"""_144.py

PIDControlNodalComponent
"""
from mastapy.nodal_analysis.nodal_entities import _141
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PID_CONTROL_NODAL_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'PIDControlNodalComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('PIDControlNodalComponent',)


class PIDControlNodalComponent(_141.NodalComponent):
    """PIDControlNodalComponent

    This is a mastapy class.
    """

    TYPE = _PID_CONTROL_NODAL_COMPONENT

    class _Cast_PIDControlNodalComponent:
        """Special nested class for casting PIDControlNodalComponent to subclasses."""

        def __init__(self, parent: 'PIDControlNodalComponent'):
            self._parent = parent

        @property
        def nodal_component(self):
            return self._parent._cast(_141.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def pid_control_nodal_component(self) -> 'PIDControlNodalComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PIDControlNodalComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PIDControlNodalComponent._Cast_PIDControlNodalComponent':
        return self._Cast_PIDControlNodalComponent(self)
