from oops_project import chatbook 

user1 = chatbook()
print(user1.id)

user2 = chatbook()
print(user2.id)

chatbook.set_id(11)

user3 = chatbook()
print(user3.id)