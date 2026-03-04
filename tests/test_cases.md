</> Markdown

# Test Cases - API Users

## TC_API_001 Create user (valid)
**Preconditions:** API running, DB available, user with username "ola" does not exist

**Steps:**
1. POST `/users` with valid JSON `{ "username":"ola", "role":"user" }`
2. Verify status code = 200
3. Verify response body contains:`id` (integer,>0), username = "ola", role = "user")
4. Verify DB contains new row (SQL: `SELECT id, username, role FROM users WHERE username="ola"`)

**Expected result:** user is created, response data is correct and user is persisted in DB

## TC_API_002 Create user (missing field)
**Preconditions:** API running, DB available
**Steps:**
1. POST `/users` with valid JSON '{ "username":"marek" }'
**Expected:** 
- Status code = 422 
- Response body contains validation error for role
- User is not created in the database (SQL: SELECT * FROM users WHERE username = "marek")

## TC_API_003 Create user with empty username
**Preconditions:** API running, DB available
**Steps:**
1. POST `/users` with valid JSON `{ "username": "", "role":"admin" }
**Expected result:**
- Status code = 422
- Response body contains validation error for username
- User is not created in the database (SQL: SELECT * FROM users WHERE role = "admin" AND username = "";)     

### TC_API_004 Create user (duplicate username)
**Preconditions:** API running, DB available, user with username "adam" already exists
**Steps:**
1. SQL: SELECT COUNT(*) FROM users WHERE username = "adam";
2. POST `/users` {"username":"adam","role":"user"}
**Expected result:** 
- Status code = 409
- JSON response body { "detail": "username already exists" }
- Number of records for username "adam" in DB does not change (SQL: SELECT COUNT(*) FROM users WHERE username = "adam")

## TC_API_005 Get user by existing ID
**Preconditions:** API running, DB available, User with `id` = "1" exists in database
**Steps:**
1. Send GET request to `/users/1`
**Expected result:**
- Status code = 200,  
- Response body contains correct user data

## TC_API_006 Get user by non-existing ID
**Preconditions:** API running
**Steps:**
1. Send GET request to `/users/9999`
**Expected result:**
- Status code = 404
- Response body: JSON { "detail":"user not found" }

## TC_API_007 Get user with invalid ID type
**Preconditions:** API running
**Steps:**
1. Send GET request to `/users/abc`
**Expected result:**
- Status code = 422
- Validation error for path parameter id

## TC_API_008 Get user with negative ID
**Preconditions:** API running
**Steps:**
1. Send GET request to `/users/-1`
**Expected result:**
- Status code = 404
- Response body: JSON { "detail": "user not found" }
