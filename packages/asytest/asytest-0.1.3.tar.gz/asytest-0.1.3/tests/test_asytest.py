from src.asytest import asytest

def test_asytest_runs_succesfully():
    test_results = asytest.run_tests("example_tests")
    assert len(test_results) == 5