from enumerate.permute import *

def test_one():
  v = [1,1,2,2,3,3]
  lst = list(knuth_lexical_permute(v))
  assert len(lst) == 90

def test_two():
  v = [1,2,3]
  lst = list(knuth_lexical_permute(v))
  assert len(lst) == 6

def test_three():
  v = [1,2,3,4,5,6]
  lst = list(knuth_lexical_permute(v))
  assert len(lst) == 720

def test_three_unsorted():
  v = [1,2,6,5,3,4]
  lst = list(knuth_lexical_permute(v))
  assert len(lst) == 720
