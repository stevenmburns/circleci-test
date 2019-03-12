from hypothesis import given, example, settings
import hypothesis.strategies as st

from enumerate.permute import *


def fact(n):
  if n == 0:
    return 1
  else:
    return n*fact(n-1)

@given(st.integers(1,8))
@example(1)
def test_no_duplicates(n):
  v = list(range(1,n+1))
  lst = list(knuth_lexical_permute(v))

  for vv in lst:
    vv.sort()
    assert v == vv

  assert len(lst) == fact(n)

@settings(max_examples=1000)
@given(st.lists(st.integers(1,8)))
def test_duplicates(dups):

  v = []
  for (idx,i) in enumerate(dups):
    for _ in range(i):
      v.append( idx+1)

  if len(v) == 0: return
  if len(v) > 8: return

  v.sort()
  print(dups,v)

  tbl = {}
  for x in v:
    if x not in tbl: tbl[x] = 0
    tbl[x] += 1

  prod = fact(len(v))
  for (_,d) in tbl.items():
    prod //= fact(d)

  lst = list(knuth_lexical_permute(v))

  assert len(lst) == prod

  for vv in lst:
    vv.sort()
    assert v == vv
