Examples for API calls:
**User registration**
curl -X POST -H "Content-type: application/json" -d '{
        "username": "user_two",
        "password1": "supersecretpassword123",
        "password2": "supersecretpassword123"
    }' 'http://localhost:8080/api/auth/register/' | jq

**Login**
curl -XPOST -H "Content-type: application/json" -d '{
      "username": "user_two",
      "password": "supersecretpassword123"
  }' 'http://localhost:8000/api/auth/login/' | jq

**Logout**
curl -XPOST -H 'Authorization: Token' \
   -H "Content-type: application/json" 'http://localhost:8000/api/auth/logout/' | jq


**TODOs**
**list todos**
curl -X GET -H 'Authorization: Token <token>' \
          -H "Content-type: application/json" 'http://127.0.0.1:8080/api/v1/list-todos/' | jq

**Ordering Todos**
curl -X GET -H 'Authorization: Token <token>' \
          -H "Content-type: application/json" 'http://127.0.0.1:8080/api/v1/list-todos/?ordering=priority,description' | jq
