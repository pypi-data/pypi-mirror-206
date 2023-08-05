"""_327.py

GearSetOptimisationResults
"""
from typing import List
from datetime import datetime

from mastapy._internal import constructor, conversion
from mastapy.gears import _326
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISATION_RESULTS = python_net_import('SMT.MastaAPI.Gears', 'GearSetOptimisationResults')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimisationResults',)


class GearSetOptimisationResults(_0.APIBase):
    """GearSetOptimisationResults

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISATION_RESULTS

    class _Cast_GearSetOptimisationResults:
        """Special nested class for casting GearSetOptimisationResults to subclasses."""

        def __init__(self, parent: 'GearSetOptimisationResults'):
            self._parent = parent

        @property
        def gear_set_optimisation_results(self) -> 'GearSetOptimisationResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetOptimisationResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def optimiser_settings_report_table(self) -> 'str':
        """str: 'OptimiserSettingsReportTable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OptimiserSettingsReportTable

        if temp is None:
            return ''

        return temp

    @property
    def report(self) -> 'str':
        """str: 'Report' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Report

        if temp is None:
            return ''

        return temp

    @property
    def results(self) -> 'List[_326.GearSetOptimisationResult]':
        """List[GearSetOptimisationResult]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def run_time(self) -> 'datetime':
        """datetime: 'RunTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RunTime

        if temp is None:
            return None

        value = conversion.pn_to_mp_datetime(temp)
        return value

    def delete_all_results(self):
        """ 'DeleteAllResults' is the original name of this method."""

        self.wrapped.DeleteAllResults()

    @property
    def cast_to(self) -> 'GearSetOptimisationResults._Cast_GearSetOptimisationResults':
        return self._Cast_GearSetOptimisationResults(self)
