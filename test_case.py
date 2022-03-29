import divisblity
import pytest

@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False),])

def test_divby5(num,output):
    # a = 10
    out1 = divisblity.divby5(num)
    assert out1 == output

@pytest.mark.parametrize("num1,output1",[(7,True),(14,True),(30,True)])
def test_divby7(num1,output1):
    # a = 10
    out1 = divisblity.divby7(num1)
    assert out1 == output1

@pytest.mark.parametrize("num2,output2",[(9,True),(18,True),(17,True)])
def test_divby9(num2,output2):
    # a = 10
    out1 = divisblity.divby9(num2)
    assert out1 == output2


@pytest.mark.parametrize("num3,output3",[(11,True),(121,True),(25,False)])
def test_divby11(num3,output3):
    # a = 10
    out1 = divisblity.divby11(num3)
    assert out1 == output3
