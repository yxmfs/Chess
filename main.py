#!/usr/bin/env python3
from man import base
bm = base.BaseMan([1,1])
print('now it is pos is :{0}'.format(bm.pos))
print('the next pos may be :{0}'.format(bm.nextsteps()))
