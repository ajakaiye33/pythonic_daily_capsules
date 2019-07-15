# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>


doo = "hi())("
open = '('
close = ')'
twin = open + close
frst = doo.count('(')
scd = doo.count(')')
numtwin = doo.count(twin)
print(frst) + print(scd)
print(numtwin)
