from hypothesis import given, example
import hypothesis.strategies as st

from tally.tally import *

@given(st.lists(st.booleans()))
@example([])
@example([True])
@example([True,True])
@example([False])
@example([False,False])
def test_at_most_one_alt_hypothesis(lst):
  s = Tally()
  mgr = VarMgr( s)
  a = mgr.add_var( BitVec( s, 'a', len(lst)))

  print("lst:", lst)

  for (idx,v) in enumerate(lst):
    if v:
      s.emit_always(a.var(idx))
    else:
      s.emit_never(a.var(idx))

  s.emit_at_most_one_alt( a.vars)

  s.solve()

  if len( [v for v in lst if v]) <= 1:
    assert s.state == 'SAT'
  else:
    assert s.state == 'UNSAT'

@given(st.lists(st.booleans()))
@example([])
@example([True])
@example([True,True])
@example([False])
@example([False,False])
def test_tally_hypothesis(lst):
  s = Tally()
  mgr = VarMgr( s)
  a = mgr.add_var( BitVec( s, 'a', len(lst)))
  b = mgr.add_var( BitVec( s, 'b', len(lst)))

  tally = len([v for v in lst if v])
  print("lst:", lst, tally)

  if tally > 0:
    s.emit_always(b.var(tally-1))
  if tally < len(lst):
    s.emit_never(b.var(tally))

  s.emit_tally( a.vars, b.vars)
  s.solve()
  assert s.state == 'SAT'
