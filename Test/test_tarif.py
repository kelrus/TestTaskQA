import pytest
import Parser
import EmulationApiService


@pytest.mark.parametrize("requestCase , expectedResult", Parser.get_test_cases())
def test_request_responce(requestCase, expectedResult):
    reqResult = EmulationApiService.emulation_request(requestCase)
    assert reqResult == expectedResult