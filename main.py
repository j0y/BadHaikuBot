import pikabu
import credentials

api = pikabu.Api(login=credentials.login, password=credentials.password)
hot = api.posts.get("hot",0)
for post in hot:
	print post.id
