"""_779.py

ConicalMeshManufacturingAnalysis
"""
from typing import List

from mastapy.gears.load_case.conical import _882
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.bevel import _790, _774
from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingAnalysis',)


class ConicalMeshManufacturingAnalysis(_1217.GearMeshImplementationAnalysis):
    """ConicalMeshManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_ANALYSIS

    class _Cast_ConicalMeshManufacturingAnalysis:
        """Special nested class for casting ConicalMeshManufacturingAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalMeshManufacturingAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(self):
            return self._parent._cast(_1217.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_analysis(self) -> 'ConicalMeshManufacturingAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_mesh_load_case(self) -> '_882.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tca(self) -> '_790.EaseOffBasedTCA':
        """EaseOffBasedTCA: 'TCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TCA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_774.ConicalMeshedGearManufacturingAnalysis]':
        """List[ConicalMeshedGearManufacturingAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis':
        return self._Cast_ConicalMeshManufacturingAnalysis(self)
