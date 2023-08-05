"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1425 import KeyedJointDesign
    from ._1426 import KeyTypes
    from ._1427 import KeywayJointHalfDesign
    from ._1428 import NumberOfKeys
