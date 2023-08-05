"""_1424.py

ShaftHubConnectionRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.detailed_rigid_connectors import _1375
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Rating', 'ShaftHubConnectionRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionRating',)


class ShaftHubConnectionRating(_0.APIBase):
    """ShaftHubConnectionRating

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_RATING

    class _Cast_ShaftHubConnectionRating:
        """Special nested class for casting ShaftHubConnectionRating to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionRating'):
            self._parent = parent

        @property
        def agma6123_spline_joint_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1412
            
            return self._parent._cast(_1412.AGMA6123SplineJointRating)

        @property
        def din5466_spline_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1414
            
            return self._parent._cast(_1414.DIN5466SplineRating)

        @property
        def gbt17855_spline_joint_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1416
            
            return self._parent._cast(_1416.GBT17855SplineJointRating)

        @property
        def sae_spline_joint_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1418
            
            return self._parent._cast(_1418.SAESplineJointRating)

        @property
        def spline_joint_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1420
            
            return self._parent._cast(_1420.SplineJointRating)

        @property
        def keyway_rating(self):
            from mastapy.detailed_rigid_connectors.keyed_joints.rating import _1430
            
            return self._parent._cast(_1430.KeywayRating)

        @property
        def interference_fit_rating(self):
            from mastapy.detailed_rigid_connectors.interference_fits.rating import _1437
            
            return self._parent._cast(_1437.InterferenceFitRating)

        @property
        def shaft_hub_connection_rating(self) -> 'ShaftHubConnectionRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_rating_information(self) -> 'str':
        """str: 'AdditionalRatingInformation' is the original name of this property."""

        temp = self.wrapped.AdditionalRatingInformation

        if temp is None:
            return ''

        return temp

    @additional_rating_information.setter
    def additional_rating_information(self, value: 'str'):
        self.wrapped.AdditionalRatingInformation = str(value) if value else ''

    @property
    def joint_design(self) -> '_1375.DetailedRigidConnectorDesign':
        """DetailedRigidConnectorDesign: 'JointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JointDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'ShaftHubConnectionRating._Cast_ShaftHubConnectionRating':
        return self._Cast_ShaftHubConnectionRating(self)
