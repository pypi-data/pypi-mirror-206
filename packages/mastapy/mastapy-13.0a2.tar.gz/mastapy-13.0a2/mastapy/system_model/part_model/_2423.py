"""_2423.py

BoltedJoint
"""
from mastapy.bolts import _1466
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2456
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BoltedJoint')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJoint',)


class BoltedJoint(_2456.SpecialisedAssembly):
    """BoltedJoint

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT

    class _Cast_BoltedJoint:
        """Special nested class for casting BoltedJoint to subclasses."""

        def __init__(self, parent: 'BoltedJoint'):
            self._parent = parent

        @property
        def specialised_assembly(self):
            return self._parent._cast(_2456.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2414
            
            return self._parent._cast(_2414.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def bolted_joint(self) -> 'BoltedJoint':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltedJoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def detailed_bolted_joint(self) -> '_1466.DetailedBoltedJointDesign':
        """DetailedBoltedJointDesign: 'DetailedBoltedJoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DetailedBoltedJoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BoltedJoint._Cast_BoltedJoint':
        return self._Cast_BoltedJoint(self)
