"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._5642 import AbstractAssemblyStaticLoadCaseGroup
    from ._5643 import ComponentStaticLoadCaseGroup
    from ._5644 import ConnectionStaticLoadCaseGroup
    from ._5645 import DesignEntityStaticLoadCaseGroup
    from ._5646 import GearSetStaticLoadCaseGroup
    from ._5647 import PartStaticLoadCaseGroup
