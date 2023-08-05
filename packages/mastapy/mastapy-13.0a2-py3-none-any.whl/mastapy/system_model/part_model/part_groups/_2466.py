"""_2466.py

ConcentricOrParallelPartGroup
"""
from mastapy.system_model.part_model.part_groups import _2471
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_OR_PARALLEL_PART_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.PartGroups', 'ConcentricOrParallelPartGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ConcentricOrParallelPartGroup',)


class ConcentricOrParallelPartGroup(_2471.PartGroup):
    """ConcentricOrParallelPartGroup

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_OR_PARALLEL_PART_GROUP

    class _Cast_ConcentricOrParallelPartGroup:
        """Special nested class for casting ConcentricOrParallelPartGroup to subclasses."""

        def __init__(self, parent: 'ConcentricOrParallelPartGroup'):
            self._parent = parent

        @property
        def part_group(self):
            return self._parent._cast(_2471.PartGroup)

        @property
        def concentric_part_group(self):
            from mastapy.system_model.part_model.part_groups import _2467
            
            return self._parent._cast(_2467.ConcentricPartGroup)

        @property
        def parallel_part_group(self):
            from mastapy.system_model.part_model.part_groups import _2470
            
            return self._parent._cast(_2470.ParallelPartGroup)

        @property
        def concentric_or_parallel_part_group(self) -> 'ConcentricOrParallelPartGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConcentricOrParallelPartGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup':
        return self._Cast_ConcentricOrParallelPartGroup(self)
