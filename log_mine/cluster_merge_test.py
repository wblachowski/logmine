import unittest
from .cluster_merge import ClusterMerge


class TestClusterMerge(unittest.TestCase):
    def test(self):
        config = {'k1': 1, 'k2': 1, 'max_dist': 0.01}
        merger = ClusterMerge(config)
        result = [
            [['a', 'b', 'c'], 1, [], ['1']],
            [['x', 'y', 'z'], 3, [], ['2', '3', '4']],
        ]
        merger.merge(
            result,
            [
                [['a', 'b', 'c'], 5, [], ['5', '6', '7', '8', '9']],
                [['m', 'n', 'p'], 2, [], ['10', '11']],
            ],
        )
        self.assertEqual(result, [
            [['a', 'b', 'c'], 6, [], ['1', '5', '6', '7', '8', '9']],
            [['x', 'y', 'z'], 3, [], ['2', '3', '4']],
            [['m', 'n', 'p'], 2, [], ['10', '11']]
        ])

    def test_merge_with_pattern(self):
        config = {'k1': 1, 'k2': 1, 'max_dist': 0.01}
        merger = ClusterMerge(config)
        result = [
            [['a', 'b', 'c'], 1, ['a', 'b', 'XXX'], ['1']],
            [['x', 'y', 'z'], 3, ['x', 'y', 'XXX'], ['2', '3', '4']],
        ]
        merger.merge(
            result,
            [
                [['a', 'b', 'c'], 5, ['a', 'b', 'XXX'], ['5', '6', '7', '8', '9']],
                [['m', 'n', 'p'], 2, ['m', 'n', 'XXX'], ['10', '11']],
            ],
        )
        self.assertEqual(result, [
            [['a', 'b', 'c'], 6, ['a', 'b', 'XXX'], ['1', '5', '6', '7', '8', '9']],
            [['x', 'y', 'z'], 3, ['x', 'y', 'XXX'], ['2', '3', '4']],
            [['m', 'n', 'p'], 2, ['m', 'n', 'XXX'], ['10', '11']]
        ])
