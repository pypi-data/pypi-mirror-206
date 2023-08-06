import pytest
import json
import responses

from pytos2.securetrack.join_cloud import JoinCloud
from pytos2.utils import get_api_node


class TestJoinCloud:
    cloud = json.load(open("tests/securetrack/json/join_clouds/cloud-67.json"))

    @responses.activate
    def test_add_join_cloud_200(self, st):
        """Add cloud"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/join/clouds",
            status=201,
        )

        """Add single cloud"""
        newCloud = st.add_join_cloud(self.cloud)
        assert newCloud == None

    @responses.activate
    def test_add_join_cloud_400(self, st):
        """Add cloud"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/join/clouds",
            status=400,
        )

        """Add single cloud"""
        with pytest.raises(ValueError) as exception:
            st.add_join_cloud(self.cloud)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_add_join_cloud_404(self, st):
        """Add cloud"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/join/clouds",
            status=404,
        )

        """Add single cloud"""
        with pytest.raises(ValueError) as exception:
            st.add_join_cloud(self.cloud)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_join_cloud(self, st, join_cloud_mock):
        """Get cloud by device id"""
        join_cloud = JoinCloud.kwargify(self.cloud)
        cloudByInt = st.get_join_cloud(67)
        cloudByStr = st.get_join_cloud("67")
        assert cloudByInt == join_cloud
        assert cloudByStr == join_cloud

        with pytest.raises(ValueError) as exception:
            st.get_join_cloud(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_join_cloud("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_update_join_cloud_200(self, st):
        """Update cloud"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/join/clouds",
            status=200,
        )

        """Update single cloud"""
        newCloud = st.update_join_cloud(self.cloud)
        assert newCloud == None

    @responses.activate
    def test_update_join_cloud_400(self, st):
        """PUT bad request"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/join/clouds",
            status=400,
        )

        with pytest.raises(ValueError) as exception:
            st.update_join_cloud(self.cloud)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_update_join_cloud_404(self, st):
        """PUT device id not found"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/join/clouds",
            status=404,
        )

        with pytest.raises(ValueError) as exception:
            st.update_join_cloud(self.cloud)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_join_cloud(self, st, join_cloud_mock):
        """Delete cloud by cloud id"""
        cloudByInt = st.delete_join_cloud(67)
        cloudByStr = st.delete_join_cloud("67")
        assert cloudByInt == None
        assert cloudByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_join_cloud(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_join_cloud("404")
        assert "Not Found" in str(exception.value)
