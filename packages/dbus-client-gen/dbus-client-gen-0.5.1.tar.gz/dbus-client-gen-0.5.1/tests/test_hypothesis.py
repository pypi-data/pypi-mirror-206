"""
Hypothesis-based tests of class generation code.
"""

# isort: STDLIB
import unittest
from os import sys

# isort: THIRDPARTY
from hypothesis import HealthCheck, given, settings
from hypothesis.strategies import tuples

# isort: LOCAL
from dbus_client_gen import managed_object_class, mo_query_builder
from dbus_client_gen._errors import (
    DbusClientMissingInterfaceError,
    DbusClientMissingPropertyError,
    DbusClientMissingSearchPropertiesError,
    DbusClientUniqueResultError,
    DbusClientUnknownSearchPropertiesError,
)

# isort considers this third party, but it is not
from tests._introspect import interface_strategy  # isort:skip

settings.register_profile("tracing", deadline=None)
if sys.gettrace() is not None:
    settings.load_profile("tracing")


class TestCase(unittest.TestCase):
    """
    Test the behavior of various auto-generated classes
    """

    @given(
        # pylint: disable=no-member
        # pylint: disable=no-value-for-parameter
        interface_strategy(
            max_children=3,
            max_methods=1,
            min_properties=1,
            max_properties=3,
            max_signals=1,
            dbus_signature_args={
                "max_codes": 3,
                "max_complete_types": 3,
                "max_struct_len": 3,
            },
        ).map(lambda x: x.element())
    )
    @settings(max_examples=20, suppress_health_check=[HealthCheck.too_slow])
    def test_managed_object(self, spec):
        """
        Test that the GMO object has the correct set of properties.
        """
        interface_name = spec.attrib["name"]

        klass = managed_object_class(interface_name, spec)

        property_names = [p.attrib["name"] for p in spec.findall("./property")]
        self.assertTrue(all(hasattr(klass, name) for name in property_names))

        with self.assertRaises(DbusClientMissingInterfaceError):
            obj = klass({})

        obj = klass({interface_name: {}})
        for name in property_names:
            with self.assertRaises(DbusClientMissingPropertyError):
                getattr(obj, name)()

        for name in property_names:
            obj = klass({interface_name: {name: True}})
            self.assertTrue(getattr(obj, name)())

    @given(
        # pylint: disable=no-member
        # pylint: disable=no-value-for-parameter
        tuples(
            interface_strategy(
                max_children=3,
                max_properties=0,
                max_methods=1,
                max_signals=1,
                dbus_signature_args={
                    "max_codes": 3,
                    "max_complete_types": 3,
                    "max_struct_len": 3,
                },
            ).map(lambda x: x.element()),
            interface_strategy(
                max_children=3,
                min_properties=1,
                max_properties=3,
                max_methods=1,
                max_signals=1,
                dbus_signature_args={
                    "max_codes": 3,
                    "max_complete_types": 3,
                    "max_struct_len": 3,
                },
            ).map(lambda x: x.element()),
        )
    )
    @settings(max_examples=5, suppress_health_check=[HealthCheck.too_slow])
    def test_managed_object_query(self, specs):
        """
        Test that the query returns appropriate values for its query input.
        """
        for spec in specs:
            interface_name = spec.attrib["name"]

            query_builder = mo_query_builder(spec)

            properties = [p.attrib["name"] for p in spec.findall("./property")]

            with self.assertRaises(DbusClientUniqueResultError):
                query_builder({}).require_unique_match().search({})

            with self.assertRaises(DbusClientUnknownSearchPropertiesError):
                query_builder({"".join(properties) + "_": True})

            query = query_builder(dict((p, True) for p in properties))
            if properties == []:
                self.assertEqual(
                    list(query.search({"op": {interface_name: {}}})),
                    [("op", {interface_name: {}})],
                )
                self.assertEqual(list(query.search({"op": {}})), [])

            else:
                with self.assertRaises(DbusClientMissingSearchPropertiesError):
                    list(query.search({"op": {interface_name: {}}}))
