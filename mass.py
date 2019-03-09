import tweepy;

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth);

username = input("type in the username of the user to tweet at")
user = api.get_user(username);
message = input("Type the message to send to the tweeters")
for friend in user.friends():
   status = api.update_status("@" + friend.screen_name + " " + message);