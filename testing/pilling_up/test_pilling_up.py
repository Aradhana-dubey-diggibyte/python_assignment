
from srs.pilling_up.util import can_stack_cubes

def test_can_stack_cubes():
    assert can_stack_cubes([4, 3, 2, 1, 3, 4]) == "Yes"
    assert can_stack_cubes([1, 3, 2]) == "No"
    assert can_stack_cubes([1]) == "Yes"
    assert can_stack_cubes([3, 3, 3, 3]) == "Yes"
    assert can_stack_cubes([1, 2, 3, 4]) == "No"
