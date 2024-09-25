from instabot import Bot

bot=Bot()
bot.login(username="id",password="password")#establish connection with the databse of instagram with given id and password of the account from which all the function are to be performed 
bot.follow("username")#follow function use to follow the username by the above logged id
bot.unfollow("username")#unfollow function use to unfollow the username from the aboved logged id

#functions for posting photo video using the above logged user id 
bot.upload_photo("location of file in your machine")
bot.upload_story_photo("location of file in your machine")
bot.upload_video("location of file in your machine")

#function to send text message
bot.send_message("message text","username_of_reciver")

#Follower list 
followers=bot.get_user_followers("username") 
#print followers list with their info
for follower in followers:
    print(bot.get_user_info("follower"))

#Following list
following=bot.get_user_info("username")
#print the following user list with info
for Following in following:
    print(bot.get_user_info("Following"))





