class User:
  def __init__(self, username):
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self, user):
    user.followers += 1
    self.following += 1

user_1 = User("Juan")
user_2 = User("Steph")
user_3 = User("Cris")

user_1.follow(user_2)
user_3.follow(user_1)
user_3.follow(user_2)

print('user1')
print(user_1.followers)
print(user_1.following)
print('user2')
print(user_2.followers)
print(user_2.following)
print('user3')
print(user_3.followers)
print(user_3.following)