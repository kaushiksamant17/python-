class Person1:
    def __init__(kk,name,surname,dob):
        kk.name1 = name
        kk.surname1 = surname
        kk.dob1 = dob

    def age(kk,current_age):
        kk.cage = current_age
        return(kk.cage - kk.dob1)


per1 = Person1("an..k..i","Ra..y",2000)
print(per1.name1)
print(per1.surname1)
print(per1.age(1989))

