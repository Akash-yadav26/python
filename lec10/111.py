# lst = [1,[2,3]]*2
# lst[0][1]=4
# print(lst)

# d ={"x":2}
# d.update({"y":d["x"]})
# d["x"] += 1
# print(d)

# t=(10,20,30)
# print(t.index(20))
# lst =[1,2,[3,4,5],6]
# print(lst[2][:-1])
# txt = "cat"
# print(txt.center(10,"*"))
# d = {"a": 3,"b" : 4}
# del d["a"]
# d["c"] = d.get("a",0)+ d.get("b")
# print(d)
# d={"a":3}
# d["b"] = d.get("a",0)*d.setdefault("c",2)
# print(d)
# my = [1,2,3,4]
# print(my[1]+my[3])
# t= (1,(2,3),4)
# res= t[1] + (5,6)
# print(res)
# t = "Python"
# print(t.endswith("n"))
# t=(1,[2,3])
# t[1].insert(1,4)
# print(t)
# my ={1,2,3}
# print(type(my))
# t =(1,2,[3,4])
# t[2][0]=5
# print(t)
lst=[1,2,3]
lst[2:]=[lst]
print(lst[2][0][1])