"""_2468.py

ConcentricPartGroupParallelToThis
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.part_groups import _2466
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_PART_GROUP_PARALLEL_TO_THIS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.PartGroups', 'ConcentricPartGroupParallelToThis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConcentricPartGroupParallelToThis',)


class ConcentricPartGroupParallelToThis(_0.APIBase):
    """ConcentricPartGroupParallelToThis

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_PART_GROUP_PARALLEL_TO_THIS

    class _Cast_ConcentricPartGroupParallelToThis:
        """Special nested class for casting ConcentricPartGroupParallelToThis to subclasses."""

        def __init__(self, parent: 'ConcentricPartGroupParallelToThis'):
            self._parent = parent

        @property
        def concentric_part_group_parallel_to_this(self) -> 'ConcentricPartGroupParallelToThis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConcentricPartGroupParallelToThis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self) -> 'float':
        """float: 'CentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def parallel_group(self) -> '_2466.ConcentricOrParallelPartGroup':
        """ConcentricOrParallelPartGroup: 'ParallelGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParallelGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConcentricPartGroupParallelToThis._Cast_ConcentricPartGroupParallelToThis':
        return self._Cast_ConcentricPartGroupParallelToThis(self)
