import pikabu
import credentials

api = pikabu.Api(login=credentials.login, password=credentials.password)
posts = api.posts.get("new",0)
for post in posts:
	print post.id
