from srs.time_delta.util import time_difference

def test_sample_cases():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
    assert time_difference(t1, t2) == 25200

    t3 = "Sat 02 May 2015 19:54:36 +0530"
    t4 = "Fri 01 May 2015 13:54:36 -0000"
    assert time_difference(t3, t4) == 88200
