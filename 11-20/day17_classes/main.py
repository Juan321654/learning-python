class User:
    def __init__(self, user_id, username): # self is an object, e.g object.id, object.username
        # the left side can be named w.e you want, does not have to match assigment
        self.id = user_id
        self.username = username
        self.followers = 0  # default values, in this case, all new accounts start with 0 followers
        self.following = 0

    def follow(self, user): #always needs "self" or "object" as the first parameter
        user.followers += 1
        self.following += 1

# user_1.id = "001"
# user_1.username = "Juan"
user_1 = User("001", "Juan")
user_2 = User("002", "Pain")

# print(user_1.id)

user_1.follow(user_2)

print("followers for user_1: ",user_1.followers)
print("followers for user_2: ",user_2.followers)

print("user_1 following: ",user_1.following)
print("user_2 following: ",user_2.following)

class Singer:
  def __init__(self, id, name):
      self.id = id
      self.name = name
      self.following = 0
      self.followers = 0

  def follow(self, singer):
    self.following += 1
    singer.followers += 1

michael = Singer("001", "Michael")
canibus = Singer("001", "Jermaine")

michael.follow(canibus)

print(canibus.followers)