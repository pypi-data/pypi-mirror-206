"""_128.py

BarRigidMBD
"""
from mastapy.nodal_analysis.nodal_entities import _127
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_RIGID_MBD = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'BarRigidMBD')


__docformat__ = 'restructuredtext en'
__all__ = ('BarRigidMBD',)


class BarRigidMBD(_127.BarMBD):
    """BarRigidMBD

    This is a mastapy class.
    """

    TYPE = _BAR_RIGID_MBD

    class _Cast_BarRigidMBD:
        """Special nested class for casting BarRigidMBD to subclasses."""

        def __init__(self, parent: 'BarRigidMBD'):
            self._parent = parent

        @property
        def bar_mbd(self):
            return self._parent._cast(_127.BarMBD)

        @property
        def component_nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _132
            
            return self._parent._cast(_132.ComponentNodalComposite)

        @property
        def nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _142
            
            return self._parent._cast(_142.NodalComposite)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def bar_rigid_mbd(self) -> 'BarRigidMBD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BarRigidMBD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BarRigidMBD._Cast_BarRigidMBD':
        return self._Cast_BarRigidMBD(self)
