class person:

    def age4(self,c_year,yob):
        return c_year - yob

    def email(self,email_id):
        print("mail id is ",email_id)

    def ask_name(self):
        name = input("tell your name")
        return name

kk = person()

bb = person()
bb.email("try@gmail.com")

print(kk.age4(2022,2000))
kk.email("kashi@gmail.com")
ss =kk.ask_name()
print(ss)