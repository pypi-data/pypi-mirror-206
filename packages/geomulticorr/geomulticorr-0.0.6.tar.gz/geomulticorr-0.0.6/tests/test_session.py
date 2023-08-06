import unittest
import geopandas as gpd

import src.geomulticorr.session
import src.geomulticorr.spine

class TestSession(unittest.TestCase):

    def setUp(self):
        self.path_to_test_session = '/media/duvanelt/TD002/sandbox_gmc/vanoise'
        self.test_session = src.geomulticorr.session.Session(self.path_to_test_session)
        self.test_pzone_name = 'iseran'
        self.test_spine_id = 'ISFR730486'

    def test_is_session(self):
        self.assertIsInstance(self.test_session, src.geomulticorr.session.Session)

    def test_get_thumbs(self):
        self.assertIsInstance(self.test_session.get_thumbs(), list)
        self.assertIsInstance(self.test_session.get_thumbs(self.test_pzone_name), list)

    def test_get_pairs(self):
        self.assertIsInstance(self.test_session.get_pairs(), list)
        self.assertIsInstance(self.test_session.get_pairs(self.test_pzone_name), list)

    def test_get_pzones(self):
        self.assertIsInstance(self.test_session.get_pzones(), list)
        self.assertIsInstance(self.test_session.get_pzones(self.test_pzone_name), list)

    def test_get_geomorphs(self):
        self.assertIsInstance(self.test_session.get_geomorphs(), list)
        self.assertIsInstance(self.test_session.get_geomorphs(self.test_pzone_name), list)

    def test_get_spine(self):
        self.assertIsInstance(self.test_session.get_spine(self.test_spine_id), src.geomulticorr.spine.Spine)

    def test_get_protomap(self):
        self.assertIsInstance(self.test_session.get_protomap(), gpd.GeoDataFrame)

if __name__ == '__main__':
    unittest.main()