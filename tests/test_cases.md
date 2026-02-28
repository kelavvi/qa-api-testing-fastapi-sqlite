</> Markdown

# Test Cases - API Users

## TC_API_001 Create user (valid)
**Preconditions:** API running, DB available
**Steps:**
1. POST '/users' with valid JSON '{ "username":"ola", "role":"user" }'
2. Verify status code = 200
3. Verify response contatins 'id'
4. Verify DB contains new row (SQL: 'SELECT * FROM users;')
**Expected:** user created and persisted in DB

## TC_API_002 Create user (missing field)
**Steps:**
1. POST '/users' with '{ "username":"marek" }'
**Expected:** status code = 422, validation error

### TC_API_003 Create user (duplicate username)
**Steps:**
1. POST '/users' with username that already exists (e,g, "adam")
**Expected:** status coed = 409, 'username already exists'
