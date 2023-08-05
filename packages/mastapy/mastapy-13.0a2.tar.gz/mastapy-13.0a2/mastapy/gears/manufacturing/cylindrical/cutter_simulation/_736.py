"""_736.py

ManufacturingOperationConstraints
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MANUFACTURING_OPERATION_CONSTRAINTS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'ManufacturingOperationConstraints')


__docformat__ = 'restructuredtext en'
__all__ = ('ManufacturingOperationConstraints',)


class ManufacturingOperationConstraints(_0.APIBase):
    """ManufacturingOperationConstraints

    This is a mastapy class.
    """

    TYPE = _MANUFACTURING_OPERATION_CONSTRAINTS

    class _Cast_ManufacturingOperationConstraints:
        """Special nested class for casting ManufacturingOperationConstraints to subclasses."""

        def __init__(self, parent: 'ManufacturingOperationConstraints'):
            self._parent = parent

        @property
        def manufacturing_operation_constraints(self) -> 'ManufacturingOperationConstraints':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ManufacturingOperationConstraints.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_root_clearance_factor(self) -> 'float':
        """float: 'GearRootClearanceFactor' is the original name of this property."""

        temp = self.wrapped.GearRootClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @gear_root_clearance_factor.setter
    def gear_root_clearance_factor(self, value: 'float'):
        self.wrapped.GearRootClearanceFactor = float(value) if value else 0.0

    @property
    def gear_tip_clearance_factor(self) -> 'float':
        """float: 'GearTipClearanceFactor' is the original name of this property."""

        temp = self.wrapped.GearTipClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @gear_tip_clearance_factor.setter
    def gear_tip_clearance_factor(self, value: 'float'):
        self.wrapped.GearTipClearanceFactor = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ManufacturingOperationConstraints._Cast_ManufacturingOperationConstraints':
        return self._Cast_ManufacturingOperationConstraints(self)
