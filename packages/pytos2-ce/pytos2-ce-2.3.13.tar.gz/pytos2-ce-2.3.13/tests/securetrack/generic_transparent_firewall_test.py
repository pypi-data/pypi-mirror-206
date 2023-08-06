import pytest
import json
import responses

from pytos2.securetrack.generic_transparent_firewall import GenericTransparentFirewall
from pytos2.utils import get_api_node


class TestGenericTransparentFirewall:
    device = json.load(
        open("tests/securetrack/json/generic_transparent_firewalls/device-9.json")
    )
    firewalls = device["TransparentFirewalls"]

    @responses.activate
    def test_add_generic_transparent_firewalls_200(self, st):
        """Add one or multiple firewalls"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/transparentfw",
            status=201,
        )

        """Add single firewall"""
        newFirewall = st.add_generic_transparent_firewalls(self.firewalls[0])
        assert newFirewall == None

        """Add multiple firewalls"""
        newFirewalls = st.add_generic_transparent_firewalls(self.firewalls)
        assert newFirewalls == None

    @responses.activate
    def test_add_generic_transparent_firewalls_400(self, st):
        """Add one or multiple firewalls"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/transparentfw",
            status=400,
        )

        """Add single firewall"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_transparent_firewalls(self.firewalls[0])
        assert "Bad Request" in str(exception.value)

        """Add multiple firewalls"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_transparent_firewalls(self.firewalls)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_add_generic_transparent_firewalls_404(self, st):
        """Add one or multiple firewalls"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/transparentfw",
            status=404,
        )

        """Add single firewall"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_transparent_firewalls(self.firewalls[0])
        assert "Not Found" in str(exception.value)

        """Add multiple firewalls"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_transparent_firewalls(self.firewalls)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_generic_transparent_firewalls(
        self, st, generic_transparent_firewall_mock
    ):
        """Get firewalls by device id"""
        firewalls = [
            GenericTransparentFirewall.kwargify(d)
            for d in get_api_node(self.device, "TransparentFirewalls", listify=True)
        ]
        firewallsByInt = st.get_generic_transparent_firewalls(9)
        firewallsByStr = st.get_generic_transparent_firewalls("9")
        assert firewallsByInt == firewalls
        assert firewallsByStr == firewalls

        with pytest.raises(ValueError) as exception:
            st.get_generic_transparent_firewalls(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.get_generic_transparent_firewalls("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_update_generic_transparent_firewalls_200(self, st):
        """Update one or multiple firewalls"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/transparentfw",
            status=200,
        )

        """Update single firewall"""
        newFirewall = st.update_generic_transparent_firewalls(self.firewalls[0])
        assert newFirewall == None

        """Update multiple firewalls"""
        newFirewalls = st.update_generic_transparent_firewalls(self.firewalls)
        assert newFirewalls == None

    @responses.activate
    def test_update_generic_transparent_firewalls_400(self, st):
        """PUT bad request"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/transparentfw",
            status=400,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_transparent_firewalls(self.firewalls[0])
        assert "Bad Request" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_transparent_firewalls(self.firewalls)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_update_generic_transparent_firewalls_404(self, st):
        """PUT device id not found"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/transparentfw",
            status=404,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_transparent_firewalls(self.firewalls[0])
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_transparent_firewalls(self.firewalls)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_transparent_firewall(
        self, st, generic_transparent_firewall_mock
    ):
        """Delete firewall by firewall id"""
        firewallByInt = st.delete_generic_transparent_firewall(23)
        firewallByStr = st.delete_generic_transparent_firewall("23")
        assert firewallByInt == None
        assert firewallByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_transparent_firewall(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_transparent_firewall("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_transparent_firewalls(
        self, st, generic_transparent_firewall_mock
    ):
        """Delete firewalls by device id"""
        firewallsByInt = st.delete_generic_transparent_firewalls(9)
        firewallsByStr = st.delete_generic_transparent_firewalls("9")
        assert firewallsByInt == None
        assert firewallsByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_transparent_firewalls(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_transparent_firewalls("404")
        assert "Not Found" in str(exception.value)
