# Controller
* "The glue between the view and the business logic."
* In this project, your view is the *console*. This package should contain classes which get or present data from or to the user by making calls to the *Service* layer.



try:
    with open("data.json","r") as read_file:
        data = json.load(read_file)
        print(data['mouad']['login-info']['password'])
except FileNotFoundError:
    print("file not found")
