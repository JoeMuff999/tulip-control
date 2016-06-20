"""
Tests for the tulip.gridworld
"""

import numpy as np
import tulip.gridworld as gw
from tulip.synth import is_realizable


REFERENCE_GWFILE = """
# A very small example, realizable by itself.
6 10
*  G*
  ***  ***
         *
I  *  *  *
  ****** *
*
"""

UNREACHABLE_GOAL_GWFILE = """
4 4
**G
  **

I* *
"""

TRIVIAL_GWFILE = """
2 2
*
"""


# Module-level fixture setup
def setUp():
    np.random.seed(0)  # Make pseudorandom number sequence repeatable


class GridWorld_test:
    def setUp(self):
        self.prefix = "testworld"
        self.X = gw.GridWorld(REFERENCE_GWFILE, prefix=self.prefix)
        self.Y_testpaths = gw.GridWorld(UNREACHABLE_GOAL_GWFILE, prefix=self.prefix)

    def tearDown(self):
        self.X = None
        self.Y_testpaths = None

    def test_reachability(self):
        # Reachability is assumed to be bidirectional
        assert not self.Y_testpaths.isReachable((3,0), (0,2))
        assert not self.Y_testpaths.isReachable((0,2), (3,0))
        assert self.Y_testpaths.isReachable((1,1), (2,3))
        assert self.Y_testpaths.isReachable((2,3), (1,1))

    def test_size(self):
        assert self.X.size() == (6, 10)

    def test_copy(self):
        Z = self.X.copy()
        assert Z is not self.X
        assert Z.W is not self.X.W
        assert Z == self.X

    def test_getitem(self):
        assert self.X.__getitem__((0,0), nonbool=False) == self.prefix+"_"+str(0)+"_"+str(0)
        assert self.X.__getitem__((-1,0), nonbool=False) == self.prefix+"_"+str(5)+"_"+str(0)
        assert self.X.__getitem__((-1,-2), nonbool=False) == self.prefix+"_"+str(5)+"_"+str(8)

    def test_state(self):
        assert self.X.state((2,3), nonbool=False) == {'testworld_3_9': 0, 'testworld_1_8': 0, 'testworld_1_9': 0, 'testworld_1_4': 0, 'testworld_1_5': 0, 'testworld_1_6': 0, 'testworld_1_7': 0, 'testworld_1_0': 0, 'testworld_1_1': 0, 'testworld_1_2': 0, 'testworld_1_3': 0, 'testworld_0_5': 0, 'testworld_0_4': 0, 'testworld_0_7': 0, 'testworld_0_6': 0, 'testworld_0_1': 0, 'testworld_0_0': 0, 'testworld_0_3': 0, 'testworld_0_2': 0, 'testworld_5_7': 0, 'testworld_0_9': 0, 'testworld_0_8': 0, 'testworld_3_2': 0, 'testworld_3_3': 0, 'testworld_2_9': 0, 'testworld_2_8': 0, 'testworld_3_6': 0, 'testworld_3_7': 0, 'testworld_3_4': 0, 'testworld_3_5': 0, 'testworld_2_3': 1, 'testworld_2_2': 0, 'testworld_2_1': 0, 'testworld_2_0': 0, 'testworld_2_7': 0, 'testworld_2_6': 0, 'testworld_2_5': 0, 'testworld_2_4': 0, 'testworld_4_1': 0, 'testworld_4_0': 0, 'testworld_4_3': 0, 'testworld_4_2': 0, 'testworld_4_5': 0, 'testworld_4_4': 0, 'testworld_4_7': 0, 'testworld_4_6': 0, 'testworld_4_9': 0, 'testworld_4_8': 0, 'testworld_5_8': 0, 'testworld_5_2': 0, 'testworld_5_9': 0, 'testworld_3_0': 0, 'testworld_3_1': 0, 'testworld_5_3': 0, 'testworld_5_5': 0, 'testworld_5_0': 0, 'testworld_5_4': 0, 'testworld_5_1': 0, 'testworld_5_6': 0, 'testworld_3_8': 0}
        assert self.X.state((-1,0), nonbool=False) == {'testworld_3_9': 0, 'testworld_1_8': 0, 'testworld_1_9': 0, 'testworld_1_4': 0, 'testworld_1_5': 0, 'testworld_1_6': 0, 'testworld_1_7': 0, 'testworld_1_0': 0, 'testworld_1_1': 0, 'testworld_1_2': 0, 'testworld_1_3': 0, 'testworld_0_5': 0, 'testworld_0_4': 0, 'testworld_0_7': 0, 'testworld_0_6': 0, 'testworld_0_1': 0, 'testworld_0_0': 0, 'testworld_0_3': 0, 'testworld_0_2': 0, 'testworld_5_7': 0, 'testworld_0_9': 0, 'testworld_0_8': 0, 'testworld_3_2': 0, 'testworld_3_3': 0, 'testworld_2_9': 0, 'testworld_2_8': 0, 'testworld_3_6': 0, 'testworld_3_7': 0, 'testworld_3_4': 0, 'testworld_3_5': 0, 'testworld_2_3': 0, 'testworld_2_2': 0, 'testworld_2_1': 0, 'testworld_2_0': 0, 'testworld_2_7': 0, 'testworld_2_6': 0, 'testworld_2_5': 0, 'testworld_2_4': 0, 'testworld_4_1': 0, 'testworld_4_0': 0, 'testworld_4_3': 0, 'testworld_4_2': 0, 'testworld_4_5': 0, 'testworld_4_4': 0, 'testworld_4_7': 0, 'testworld_4_6': 0, 'testworld_4_9': 0, 'testworld_4_8': 0, 'testworld_5_8': 0, 'testworld_5_2': 0, 'testworld_5_9': 0, 'testworld_3_0': 0, 'testworld_3_1': 0, 'testworld_5_3': 0, 'testworld_5_5': 0, 'testworld_5_0': 1, 'testworld_5_4': 0, 'testworld_5_1': 0, 'testworld_5_6': 0, 'testworld_3_8': 0}
        assert self.X.state((-1,-1), nonbool=False) == {'testworld_3_9': 0, 'testworld_1_8': 0, 'testworld_1_9': 0, 'testworld_1_4': 0, 'testworld_1_5': 0, 'testworld_1_6': 0, 'testworld_1_7': 0, 'testworld_1_0': 0, 'testworld_1_1': 0, 'testworld_1_2': 0, 'testworld_1_3': 0, 'testworld_0_5': 0, 'testworld_0_4': 0, 'testworld_0_7': 0, 'testworld_0_6': 0, 'testworld_0_1': 0, 'testworld_0_0': 0, 'testworld_0_3': 0, 'testworld_0_2': 0, 'testworld_5_7': 0, 'testworld_0_9': 0, 'testworld_0_8': 0, 'testworld_3_2': 0, 'testworld_3_3': 0, 'testworld_2_9': 0, 'testworld_2_8': 0, 'testworld_3_6': 0, 'testworld_3_7': 0, 'testworld_3_4': 0, 'testworld_3_5': 0, 'testworld_2_3': 0, 'testworld_2_2': 0, 'testworld_2_1': 0, 'testworld_2_0': 0, 'testworld_2_7': 0, 'testworld_2_6': 0, 'testworld_2_5': 0, 'testworld_2_4': 0, 'testworld_4_1': 0, 'testworld_4_0': 0, 'testworld_4_3': 0, 'testworld_4_2': 0, 'testworld_4_5': 0, 'testworld_4_4': 0, 'testworld_4_7': 0, 'testworld_4_6': 0, 'testworld_4_9': 0, 'testworld_4_8': 0, 'testworld_5_8': 0, 'testworld_5_2': 0, 'testworld_5_9': 1, 'testworld_3_0': 0, 'testworld_3_1': 0, 'testworld_5_3': 0, 'testworld_5_5': 0, 'testworld_5_0': 0, 'testworld_5_4': 0, 'testworld_5_1': 0, 'testworld_5_6': 0, 'testworld_3_8': 0}


    def test_equality(self):
        assert self.X == gw.GridWorld(REFERENCE_GWFILE)
        Y = gw.GridWorld()
        assert self.X != Y
        Y = gw.GridWorld(TRIVIAL_GWFILE)
        assert self.X != Y

        # Avoid bug due to careless NumPy broadcasting
        Z3x5 = gw.unoccupied((3,5))
        Z1x1 = gw.unoccupied((1,1))
        assert Z3x5 != Z1x1


    def test_dumploadloop(self):
        assert self.X == gw.GridWorld(self.X.dumps())

    def test_spec_realizable_bool(self):
        assert is_realizable('gr1c', self.X.spec(nonbool=False))

    def test_spec_realizable(self):
        assert is_realizable('gr1c', self.X.spec())

    def check_isEmpty(self, coord, expected):
        assert self.X.isEmpty(coord) == expected

    def test_isEmpty(self):
        for coord, expected in [((0, 0), False), ((0, 1), True),
                                ((-1, 0), False), ((0, -1), True)]:
            yield self.check_isEmpty, coord, expected

    def check_isEmpty_extend(self, coord, expected):
        assert self.X.isEmpty(coord, extend=True) == expected

    def test_isEmpty_extend(self):
        for coord, expected in [((0, 0), False), ((0, 1), True),
                                ((-1, 0), False), ((0, -1), False)]:
            yield self.check_isEmpty_extend, coord, expected

    def test_dumpsubworld(self):
        # No offset
        X_local = self.X.dumpsubworld((2,4), prefix="X")
        assert X_local.size() == (2, 4)
        assert X_local.__getitem__((0,0), nonbool=False) == "X_0_0"
        assert not X_local.isEmpty((0,0))
        assert X_local.isEmpty((0,1))

        # Offset
        X_local = self.X.dumpsubworld((2,4), offset=(1,0), prefix="Xoff")
        assert X_local.size() == (2, 4)
        assert X_local.__getitem__((0,0), nonbool=False) == "Xoff_0_0"
        assert X_local.isEmpty((0,0))
        assert X_local.isEmpty((0,1))
        assert not X_local.isEmpty((0,3))

    def test_dumpsubworld_extend(self):
        # No offset
        Xsize = self.X.size()
        X_local = self.X.dumpsubworld((Xsize[0]+1, Xsize[1]), prefix="X",
                                      extend=True)
        X_local.goal_list = self.X.goal_list[:]
        X_local.init_list = self.X.init_list[:]
        assert X_local.size() == (7, 10)
        assert X_local.__getitem__((0,0), nonbool=False) == "X_0_0"
        assert not X_local.isEmpty((0,0))
        assert X_local.isEmpty((0,1))
        # Equal except for the last row, which should be all occupied in X_local
        X_local_s = X_local.dumps().splitlines()
        assert np.all(X_local_s[1:-1] == self.X.dumps().splitlines()[1:])
        assert not X_local.isEmpty((6,1))
        assert X_local_s[-1] == "*"*10

        # Offset
        X_local = self.X.dumpsubworld((3,4), offset=(-1,0), prefix="Xoff",
                                      extend=True)
        assert X_local.size() == (3, 4)
        assert X_local.__getitem__((0,0), nonbool=False) == "Xoff_0_0"
        assert not X_local.isEmpty((0,0))
        assert not X_local.isEmpty((0,1))
        assert not X_local.isEmpty((0,3))
        assert X_local.isEmpty((1,1))


class RandomWorld_test():
    def setUp(self):
        self.wall_densities = [.2, .4, .6]
        self.sizes = [(4,5), (4,5), (10,20)]
        self.rworlds = [gw.random_world(self.sizes[r], wall_density=self.wall_densities[r], prefix="Y") for r in range(len(self.sizes))]
        self.rworlds_ensuredfeasible = [gw.random_world(self.sizes[r], self.wall_densities[r], num_init=2, num_goals=2, ensure_feasible=True) for r in range(len(self.sizes))]

    def tearDown(self):
        self.rworlds = []

    def test_feasibility(self):
        for r in range(len(self.rworlds_ensuredfeasible)):
            print "test \"ensured feasible\" world index", r
            print self.rworlds_ensuredfeasible[r]
            assert self.rworlds_ensuredfeasible[r].isReachable(self.rworlds_ensuredfeasible[r].init_list[0], self.rworlds_ensuredfeasible[r].init_list[1])
            assert self.rworlds_ensuredfeasible[r].isReachable(self.rworlds_ensuredfeasible[r].init_list[1], self.rworlds_ensuredfeasible[r].goal_list[0])
            assert self.rworlds_ensuredfeasible[r].isReachable(self.rworlds_ensuredfeasible[r].goal_list[0], self.rworlds_ensuredfeasible[r].goal_list[1])
            assert self.rworlds_ensuredfeasible[r].isReachable(self.rworlds_ensuredfeasible[r].goal_list[1], self.rworlds_ensuredfeasible[r].init_list[0])

    def test_size(self):
        for r in range(len(self.rworlds)):
            print "test world index", r
            print self.rworlds[r]
            assert self.sizes[r] == self.rworlds[r].size()

    def test_density(self):
        for r in range(len(self.rworlds)):
            print "test world index", r
            print self.rworlds[r]
            (num_rows, num_cols) = self.rworlds[r].size()
            num_occupied = 0
            for i in range(num_rows):
                for j in range(num_cols):
                    if not self.rworlds[r].isEmpty((i,j)):
                        num_occupied += 1
            assert float(num_occupied)/(num_rows*num_cols) == self.wall_densities[r]

RandomWorld_test.slow = True


def extract_coord_test():
    assert gw.extract_coord("test_3_0") == ("test", 3, 0)
    assert gw.extract_coord("obstacle_5_4_11") == ("obstacle_5", 4, 11)
    assert gw.extract_coord("test3_0") is None
