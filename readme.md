# REST-API for indian banks and branches
## Endpoint 1
- https://rest-fyle.herokuapp.com/api/branches/?autocomplete=PUNE
- Replace PUNE with any other branch name to get the respective branches.
- You can set limit and offset via query parameters for example:-
- http://rest-fyle.herokuapp.com/api/branches/?autocomplete=RTGS-HO&limit=10&offset=10

## Endpoint 2
- https://rest-fyle.herokuapp.com/api/branches/?search=PUNE
- Here, replace PUNE with any information to return possible matches across all columns and all rows.

# Database
- Used AWS RDS to setup the database.

