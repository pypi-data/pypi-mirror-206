"""_865.py

ConicalMeshLoadDistributionAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.conical import _882
from mastapy.gears.manufacturing.bevel import _779
from mastapy.gears.ltca.conical import _864
from mastapy.gears.ltca import _836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalMeshLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshLoadDistributionAnalysis',)


class ConicalMeshLoadDistributionAnalysis(_836.GearMeshLoadDistributionAnalysis):
    """ConicalMeshLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_ConicalMeshLoadDistributionAnalysis:
        """Special nested class for casting ConicalMeshLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalMeshLoadDistributionAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_load_distribution_analysis(self):
            return self._parent._cast(_836.GearMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_implementation_analysis(self):
            from mastapy.gears.analysis import _1217
            
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
        def conical_mesh_load_distribution_analysis(self) -> 'ConicalMeshLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_roll_angles(self) -> 'int':
        """int: 'NumberOfRollAngles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfRollAngles

        if temp is None:
            return 0

        return temp

    @property
    def pinion_mean_te(self) -> 'float':
        """float: 'PinionMeanTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionMeanTE

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_peak_to_peak_te(self) -> 'float':
        """float: 'PinionPeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionPeakToPeakTE

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_peak_to_peak_te(self) -> 'float':
        """float: 'WheelPeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelPeakToPeakTE

        if temp is None:
            return 0.0

        return temp

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
    def conical_mesh_manufacturing_analysis(self) -> '_779.ConicalMeshManufacturingAnalysis':
        """ConicalMeshManufacturingAnalysis: 'ConicalMeshManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshManufacturingAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_864.ConicalMeshedGearLoadDistributionAnalysis]':
        """List[ConicalMeshedGearLoadDistributionAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalMeshLoadDistributionAnalysis._Cast_ConicalMeshLoadDistributionAnalysis':
        return self._Cast_ConicalMeshLoadDistributionAnalysis(self)
