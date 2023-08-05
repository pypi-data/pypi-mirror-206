"""_127.py

BarMBD
"""
from mastapy.nodal_analysis.nodal_entities import _132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_MBD = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'BarMBD')


__docformat__ = 'restructuredtext en'
__all__ = ('BarMBD',)


class BarMBD(_132.ComponentNodalComposite):
    """BarMBD

    This is a mastapy class.
    """

    TYPE = _BAR_MBD

    class _Cast_BarMBD:
        """Special nested class for casting BarMBD to subclasses."""

        def __init__(self, parent: 'BarMBD'):
            self._parent = parent

        @property
        def component_nodal_composite(self):
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
        def bar_elastic_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _126
            
            return self._parent._cast(_126.BarElasticMBD)

        @property
        def bar_rigid_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _128
            
            return self._parent._cast(_128.BarRigidMBD)

        @property
        def bar_mbd(self) -> 'BarMBD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BarMBD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BarMBD._Cast_BarMBD':
        return self._Cast_BarMBD(self)
