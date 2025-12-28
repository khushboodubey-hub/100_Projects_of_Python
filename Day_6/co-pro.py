class User:

    # we set our attributes in constructor ssame as the self parameter.
    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id 
        self.follower = 0
        self.following = 0
        print("new useer been created...")

    def follow(self, user):
        user.follower += 1
        self.following += 1
    
# user_1 = User("preeta", 24) 
# # user_1.id = "001"
# # print(user_1.id)
# print(user_1.username)
# print(user_1.id)
# print(user_1.follower)

user_1 = User("kat", 12)
user_2 = User("aaru", 9)

user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
