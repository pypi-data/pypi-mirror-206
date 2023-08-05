"""_737.py

ManufacturingProcessControls
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MANUFACTURING_PROCESS_CONTROLS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'ManufacturingProcessControls')


__docformat__ = 'restructuredtext en'
__all__ = ('ManufacturingProcessControls',)


class ManufacturingProcessControls(_0.APIBase):
    """ManufacturingProcessControls

    This is a mastapy class.
    """

    TYPE = _MANUFACTURING_PROCESS_CONTROLS

    class _Cast_ManufacturingProcessControls:
        """Special nested class for casting ManufacturingProcessControls to subclasses."""

        def __init__(self, parent: 'ManufacturingProcessControls'):
            self._parent = parent

        @property
        def manufacturing_process_controls(self) -> 'ManufacturingProcessControls':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ManufacturingProcessControls.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tooth_thickness_specification_compliance_checked(self) -> 'bool':
        """bool: 'ToothThicknessSpecificationComplianceChecked' is the original name of this property."""

        temp = self.wrapped.ToothThicknessSpecificationComplianceChecked

        if temp is None:
            return False

        return temp

    @tooth_thickness_specification_compliance_checked.setter
    def tooth_thickness_specification_compliance_checked(self, value: 'bool'):
        self.wrapped.ToothThicknessSpecificationComplianceChecked = bool(value) if value else False

    @property
    def cast_to(self) -> 'ManufacturingProcessControls._Cast_ManufacturingProcessControls':
        return self._Cast_ManufacturingProcessControls(self)
