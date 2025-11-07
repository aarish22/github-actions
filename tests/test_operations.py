from src.math_opertaions import add,sub

def test_add():
  assert add(2,4)==6
  assert add(-1,1)==0
  
def test_sub():
  assert sub(2,8)==-6
  assert sub(2,1)==1