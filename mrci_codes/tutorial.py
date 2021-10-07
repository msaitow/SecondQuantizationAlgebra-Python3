import secondQuantizationAlgebra as sqa

p = sqa.index('p')
q = sqa.index('q')
r = sqa.index('r')
s = sqa.index('s')

p_cre = sqa.creOp(p)
q_cre = sqa.creOp(q)
r_des = sqa.desOp(r)
s_des = sqa.desOp(s)

Esym   = sqa.symmetry((0,1,2,3), 1)

a = sqa.tensor("T",[p,q,r,s],[Esym])
b = sqa.tensor("R",[p,q,r,s],[Esym])

unordered = sqa.term(1.0, [], [r_des, s_des, p_cre, q_cre])

print(unordered)

#print("hoge1")
#
#kuso = sorted([s_des, r_des, q_cre, p_cre])
#
#for t in kuso: print(t)
#
#print("hoge2")
#
#(sortSign,sortedOps) = sqa.sortOps([r_des, s_des, p_cre, q_cre])
#
print("hoge3")

ordered_terms = sqa.normalOrder(unordered)

for t in ordered_terms:
  print(t)

