"""_2418.py

AxialInternalClearanceTolerance
"""
from mastapy.system_model.part_model import _2439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_INTERNAL_CLEARANCE_TOLERANCE = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AxialInternalClearanceTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialInternalClearanceTolerance',)


class AxialInternalClearanceTolerance(_2439.InternalClearanceTolerance):
    """AxialInternalClearanceTolerance

    This is a mastapy class.
    """

    TYPE = _AXIAL_INTERNAL_CLEARANCE_TOLERANCE

    class _Cast_AxialInternalClearanceTolerance:
        """Special nested class for casting AxialInternalClearanceTolerance to subclasses."""

        def __init__(self, parent: 'AxialInternalClearanceTolerance'):
            self._parent = parent

        @property
        def internal_clearance_tolerance(self):
            return self._parent._cast(_2439.InternalClearanceTolerance)

        @property
        def axial_internal_clearance_tolerance(self) -> 'AxialInternalClearanceTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AxialInternalClearanceTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AxialInternalClearanceTolerance._Cast_AxialInternalClearanceTolerance':
        return self._Cast_AxialInternalClearanceTolerance(self)
