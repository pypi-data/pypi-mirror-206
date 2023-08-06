"""Integration tests for the Destination APIs."""

from hypothesis import given

from anaml_client.models.cluster import Cluster

from base import TestBase
from generators import ClusterGen


class TestCluster(TestBase):
    @given(ClusterGen)
    def test_round_trip(self, cluster: Cluster):
        assert cluster == Cluster.from_json(cluster.to_json())
