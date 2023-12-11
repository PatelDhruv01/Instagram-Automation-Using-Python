from instabot import Bot
bot=Bot()

# login
bot.login(username="username", password="password")

# follow
bot.follow("target_username")

# upload photo
bot.upload_photo("PathWith/", caption="textForCaption")

# unfollow
bot.unfollow("target_username")

# send message
bot.send_message("msg", ["id1", "id2", "..."])

# getting follower info
followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

# getting following info
following=bot.get_user_following("username")
for Following in following:
    print(bot.get_user_info(Following))


# My trick to remove keyErrors: just delete the Config folder everytime