class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"

# print(user_1.username)

# user_2 = User()
# user_1.id = "002"
# user_1.username = "jack"


user_3 = User("003", "Bob")
user_4 = User("004", "Kevin")

print(user_3.username)


print(user_3.followers)

user_4.follow(user_3)
print(user_4.following)
print(user_3.followers)