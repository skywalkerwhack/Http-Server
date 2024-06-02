# Define the responses for different paths and methods
# Some basic Http RESPONSES like GET, PUT, DELETE, etc
# Status codes like BAD_REQUEST_RESPONSE, FORBIDDEN_RESPONSE, NOT_FOUND_RESPONSE,
#       METHOD_NOT_ALLOWED_RESPONSE;
RESPONSES = {
    'GET': {
        '/': b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is the main page.</p>
</body>
</html>
""",
        '/somewhere': b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server</title>
</head>
<body>
    <h1>Somewhere Page</h1>
    <p>You have navigated to /somewhere.</p>
</body>
</html>
"""
    },
    'POST': {
        '/post': b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server</title>
</head>
<body>
    <h1>Form Submitted</h1>
    <p>You have submitted a POST request.</p>
</body>
</html>
"""
    },
    'PUT': {
        '/put': b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server</title>
</head>
<body>
    <h1>Resource Updated</h1>
    <p>You have submitted a PUT request to update a resource.</p>
</body>
</html>
"""
    },
    'DELETE': {
        '/delete': b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server</title>
</head>
<body>
    <h1>Resource Deleted</h1>
    <p>You have submitted a DELETE request to delete a resource.</p>
</body>
</html>
"""
    }
}

# 400 Bad Request response
BAD_REQUEST_RESPONSE = b"""\
HTTP/1.1 400 Bad Request
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>400 Bad Request</title>
</head>
<body>
    <h1>400 Bad Request</h1>
    <p>The request could not be understood by the server due to malformed syntax.</p>
</body>
</html>
"""
# 403 Forbidden response
FORBIDDEN_RESPONSE = b"""\
HTTP/1.1 403 Forbidden
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>403 Forbidden</title>
</head>
<body>
    <h1>403 Forbidden</h1>
    <p>You do not have permission to access this resource.</p>
</body>
</html>
"""
# 404 Not Found response
NOT_FOUND_RESPONSE = b"""\
HTTP/1.1 404 Not Found
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The requested URL or method was not found on this server.</p>
</body>
</html>
"""
# 405 Method Not Allowed response
METHOD_NOT_ALLOWED_RESPONSE = b"""\
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>405 Method Not Allowed</title>
</head>
<body>
    <h1>405 Method Not Allowed</h1>
    <p>The requested method is not allowed for the specified URL.</p>
</body>
</html>
"""