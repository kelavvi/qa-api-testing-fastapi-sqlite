</> Markdown
# Bug fixes / Findings (mini log)

## Finding 1: Empty username accepted
**Issue:* POST '/users' accepted empty 'username' and returned 200
**Expected:* 422 validation error
**Fix:** Added validation (min_length / trimming)
**Result:** API now returns 422 for empty username

## Finding 2: Duplicate username (login) should be blocked
**Issue:** API allowed duplicate login
**Expected:** 409 Conflict
**Fix:** Added DB check before INSERT
**Result:** API returns 409 when username already exists

## Finding 3: DB locked during insert
**Issue:** 500 Internal Server Error when DB Browser kept SQLite open
**Fix.Workaround:** Close DB Browser during API writes
**Result:** POST works correctly, user is persisted in DB
