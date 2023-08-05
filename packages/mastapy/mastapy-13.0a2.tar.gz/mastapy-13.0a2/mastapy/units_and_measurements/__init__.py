"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._7522 import MeasurementType
    from ._7523 import MeasurementTypeExtensions
