from odd_even import odd_even
from sequence_sum import sequence_sum


class TestClass(object): 
    def test_odd_even(self):
        assert odd_even(3) == 'odd'
        assert odd_even(5) == 'odd'
        assert odd_even(8) == 'even'

    def test_seq_sum1(self):
       assert sequence_sum(2,2,2) == 2
     
    def test_seq_sum2(self):
       assert sequence_sum(2,4,2) == 4
       
    def test_seq_sum3(self):
       assert sequence_sum(2,6,2) == 12 
    def test_seq_sum4(self):
       assert sequence_sum(1,5,1) == 15 
    def test_seq_sum5(self):
       assert sequence_sum(1,5,3) == 5 
    def test_seq_sum6(self):
       assert sequence_sum(7,5,3) == 0 