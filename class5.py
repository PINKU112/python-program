

# example of tuple.

tup = (2,4,7,5,3,8)
print(type(tup))
print(tup[1])
print(tup[2])
print(tup)


tup = (1,)
print(tup)
print(type(tup))


tup1 = ("pinku","raju")
print(tup1)
print(type(tup1))


tup = (3,5,7,8,5,2)
print(tup[1:4])
print(tup[3:])
print(tup[:4])

tup = (1,7,5,8,5,3)
print(tup.index(3))
print(tup.count(5))
print(tup[4])


# example of dictionary

info = {
    "name" :"rahul",
    "learning" :"coding",
    "age" :23,
    "carrier" : "good"
}
print(info)
print(info["name"])
print(info["carrier"])
print(info["age"])
print(type(info))

info["name"] = "rajesh"
info["surname"] = "sahoo"
print(info)


# example of nested dictionary

student = {
    "name" : "rahul kumar",
    "subject" : {
        "java" : {
            "core-java" : 78,
            "adv java" : 87
        },
        "c++" : 67,
        "python": 99

    }
}

print(student)
print(student["name"])
print(student["subject"]["python"])
print(student["subject"]["java"]["core-java"])

# example of dictionary methods.


student1 = {
    "name" : "rahul kumar",
     "subject" : {
         "java":98,
         "c++" :67,
         "python":99
     }
}

print(info)
print(student1.keys())
print(student1["subject"].keys())
print(student1.values())
print(student1["subject"].values())
print(student1.items())
print(student1.get("subject"))
student1.update({"city":"bhubaneswar"})
print(student1)


# example of set

collection = {1,2,3,2,4,1,5,"hello","world","hello"}
print(collection)
print(type(collection))

collection = set()
print(type(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.remove(1)
collection.clear()
print(collection)

collection1 = {"hello","rahul","rajeev","biswa","world"}
print(collection1.pop())