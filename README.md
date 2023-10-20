# api_final
## About
This project based on Django REST API allows you you to receive information in JSON format about posts, comments and groups of Yatube service. Authorized users can also add posts and comments to them, modify and delete created.
## How to install
Clone the repository and navigate to it at the command line:

```
git clone https://github.com/Gustcat/api_final_yatube.git

cd api_final_yatube
```

Create and activate a virtual environment:

```
python -m venv venv

source venv/Scripts/activate
```
Install the dependencies from requirements.txt:

```
pip install -r requirements.txt
```
Execute migrations:

```
python manage.py migrate
```

Start the project:

```
python manage.py runserver
```
## Request examples
### **Creating a post**
Adding a new post to the collection of posts. Anonymous requests are not allowed.

*Request*
```
POST /api/v1/posts/ HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0MjMwNjcxLCJqdGkiOiI3NDg1YWExZGRhYmQ0NGE5OWQ5ZjJjYjEwZmNmMzkwYiIsInVzZXJfaWQiOjN9.Y8pSXzwrhREEnehWDgPXwgxmb2W16kY4X2L2FnQv4JM
Content-Type: application/json
Body:
{
"text": "string",
"image": "string",
"group": 0
}
```
*Response*
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
### **Subscriptions**
Returns all subscriptions of the user who made the request. Anonymous requests are not allowed.
Subscriptions can be searched by the "search" parameter `(GET /api/v1/follow/?search=someauthor)`

*Request*
```
GET /api/v1/follow/ HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0MjMwNjcxLCJqdGkiOiI3NDg1YWExZGRhYmQ0NGE5OWQ5ZjJjYjEwZmNmMzkwYiIsInVzZXJfaWQiOjN9.Y8pSXzwrhREEnehWDgPXwgxmb2W16kY4X2L2FnQv4JM
Content-Type: application/json
```
*Response*
```
[
    {
        "user": "user1",
        "following": "someauthor1"
    },
    {
        "user": "string",
        "following": "someauthor2"
    },
]
```
## Author
https://github.com/Gustcat
