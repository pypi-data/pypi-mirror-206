import pytest
import json
import responses

from pytos2.securetrack.generic_interface_customer import GenericInterfaceCustomer
from pytos2.utils import get_api_node


class TestGenericInterfaceCustomer:
    device = json.load(
        open("tests/securetrack/json/generic_interface_customers/device-5.json")
    )
    interfaces = device["InterfaceCustomerTags"]

    interface_customer = json.load(
        open("tests/securetrack/json/generic_interface_customers/int-cust-74.json")
    )
    interface = interface_customer["InterfaceCustomerTag"]

    @responses.activate
    def test_add_generic_interface_customers_200(self, st):
        """Add one or multiple interface customers"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/interfacecustomer",
            status=201,
        )

        """Add single interface customer"""
        newRoute = st.add_generic_interface_customer(self.interface)
        assert newRoute == None

        """Add multiple interface customers"""
        newRoutes = st.add_generic_interface_customers(self.interfaces)
        assert newRoutes == None

    @responses.activate
    def test_add_generic_interface_customers_400(self, st):
        """Add one or multiple interface customers"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/interfacecustomer",
            status=400,
        )

        """Add single interface customer"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_interface_customer(self.interface)
        assert "Bad Request" in str(exception.value)

        """Add multiple interface customers"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_interface_customers(self.interfaces)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_add_generic_interface_customers_404(self, st):
        """Add one or multiple interface customers"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/interfacecustomer",
            status=404,
        )

        """Add single interface customer"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_interface_customer(self.interface)
        assert "Not Found" in str(exception.value)

        """Add multiple interface customers"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_interface_customers(self.interfaces)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_generic_interface_customer(self, st, generic_interface_customer_mock):
        """Get interface by interface id"""
        mockRes = get_api_node(self.interface_customer, "InterfaceCustomerTag")
        interface = GenericInterfaceCustomer.kwargify(mockRes)
        interface_customerByInt = st.get_generic_interface_customer(74)
        interface_customerByStr = st.get_generic_interface_customer("74")
        assert interface_customerByInt == interface
        assert interface_customerByStr == interface

        with pytest.raises(ValueError) as exception:
            st.get_generic_interface_customer(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.get_generic_interface_customer("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_generic_interface_customers(self, st, generic_interface_customer_mock):
        """Get interfaces by device id"""
        interfaces = [
            GenericInterfaceCustomer.kwargify(d)
            for d in get_api_node(self.device, "InterfaceCustomerTags", listify=True)
        ]
        interface_customersByInt = st.get_generic_interface_customers(5)
        interface_customersByStr = st.get_generic_interface_customers("5")
        assert interface_customersByInt == interfaces
        assert interface_customersByStr == interfaces

        with pytest.raises(ValueError) as exception:
            st.get_generic_interface_customers(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.get_generic_interface_customers("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_update_generic_interface_customers_200(self, st):
        """Update one or multiple interface customers"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/interfacecustomer",
            status=200,
        )

        """Update single interface customer"""
        newRoute = st.update_generic_interface_customer(self.interface)
        assert newRoute == None

        """Update multiple interface customers"""
        newRoutes = st.update_generic_interface_customers(self.interfaces)
        assert newRoutes == None

    @responses.activate
    def test_update_generic_interface_customers_400(self, st):
        """PUT bad request"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/interfacecustomer",
            status=400,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_interface_customer(self.interface)
        assert "Bad Request" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_interface_customers(self.interfaces)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_update_generic_interface_customers_404(self, st):
        """PUT device id not found"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/interfacecustomer",
            status=404,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_interface_customer(self.interface)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_interface_customers(self.interfaces)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_interface_customer(
        self, st, generic_interface_customer_mock
    ):
        """Delete interface by interface id"""
        interface_customerByInt = st.delete_generic_interface_customer(74)
        interface_customerByStr = st.delete_generic_interface_customer("74")
        assert interface_customerByInt == None
        assert interface_customerByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interface_customer(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interface_customer("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_interface_customers(
        self, st, generic_interface_customer_mock
    ):
        """Delete interfaces by device id"""
        interface_customersByInt = st.delete_generic_interface_customers(5)
        interface_customersByStr = st.delete_generic_interface_customers("5")
        assert interface_customersByInt == None
        assert interface_customersByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interface_customers(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interface_customers("404")
        assert "Not Found" in str(exception.value)
