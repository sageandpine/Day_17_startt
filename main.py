class User:
   def __init__(self, user_id, username):
       # require these two to create object
       self.user_id = user_id
       self.username = username
       # set a default value that we know starts the same for every object
       self.followers = 0
       self.following = 0

   def follow(self,user):
       user.followers += 1
       self.following += 1

user_1 = User("001", "Jeff")
user_2 = User("002", "Stevie")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)

print(user_2.followers)
print(user_2.following)

