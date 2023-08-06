import pytest
import json
import responses

from pytos2.securetrack.generic_route import GenericRoute
from pytos2.utils import get_api_node


class TestGenericRoute:
    mgmt = json.load(open("tests/securetrack/json/generic_routes/mgmt-3.json"))
    routes = mgmt["GenericRoutes"]

    route27 = json.load(open("tests/securetrack/json/generic_routes/route-27.json"))
    route = route27["GenericRoute"]

    @responses.activate
    def test_add_generic_routes_200(self, st):
        """Add one or multiple routes"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/route",
            status=201,
        )

        """Add single route"""
        newRoute = st.add_generic_route(self.route)
        assert newRoute == None

        """Add multiple routes"""
        newRoutes = st.add_generic_routes(self.routes)
        assert newRoutes == None

    @responses.activate
    def test_add_generic_routes_400(self, st):
        """Add one or multiple routes"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/route",
            status=400,
        )

        """Add single route"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_route(self.route)
        assert "Bad Request" in str(exception.value)

        """Add multiple routes"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_routes(self.routes)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_add_generic_routes_404(self, st):
        """Add one or multiple routes"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/route",
            status=404,
        )

        """Add single route"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_route(self.route)
        assert "Not Found" in str(exception.value)

        """Add multiple routes"""
        with pytest.raises(ValueError) as exception:
            st.add_generic_routes(self.routes)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_generic_route(self, st, generic_route_mock):
        """Get route by route id"""
        mockRes = get_api_node(self.route27, "GenericRoute")
        route = GenericRoute.kwargify(mockRes)
        routeByInt = st.get_generic_route(27)
        routeByStr = st.get_generic_route("27")
        assert routeByInt == route
        assert routeByStr == route

        with pytest.raises(ValueError) as exception:
            st.get_generic_route(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.get_generic_route("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_generic_routes(self, st, generic_route_mock):
        """Get routes by mgmt id"""
        routes = [
            GenericRoute.kwargify(d)
            for d in get_api_node(self.mgmt, "GenericRoutes", listify=True)
        ]
        routesByInt = st.get_generic_routes(3)
        routesByStr = st.get_generic_routes("3")
        assert routesByInt == routes
        assert routesByStr == routes

        with pytest.raises(ValueError) as exception:
            st.get_generic_routes(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.get_generic_routes("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_update_generic_routes_200(self, st):
        """Update one or multiple routes"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/route",
            status=200,
        )

        """Update single route"""
        newRoute = st.update_generic_route(self.route)
        assert newRoute == None

        """Update multiple routes"""
        newRoutes = st.update_generic_routes(self.routes)
        assert newRoutes == None

    @responses.activate
    def test_update_generic_routes_400(self, st):
        """PUT bad request"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/route",
            status=400,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_route(self.route)
        assert "Bad Request" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_routes(self.routes)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_update_generic_routes_404(self, st):
        """PUT mgmt id not found"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/route",
            status=404,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_route(self.route)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_routes(self.routes)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_route(self, st, generic_route_mock):
        """Delete route by route id"""
        routeByInt = st.delete_generic_route(27)
        routeByStr = st.delete_generic_route("27")
        assert routeByInt == None
        assert routeByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_route(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_route("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_routes(self, st, generic_route_mock):
        """Delete routes by mgmt id"""
        routesByInt = st.delete_generic_routes(2)
        routesByStr = st.delete_generic_routes("2")
        assert routesByInt == None
        assert routesByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_routes(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_routes("404")
        assert "Not Found" in str(exception.value)
