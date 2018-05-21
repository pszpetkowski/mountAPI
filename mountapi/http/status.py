from collections import namedtuple

Status = namedtuple('Status', ['code', 'reason'])

# 2xx status codes
OK_200 = Status(200, b'OK')
CREATED_201 = Status(201, b'Created')

# 3xx status codes
MULTIPLE_CHOICES_300 = Status(300, b'Multiple Choices')
MOVED_PERMANENTLY_301 = Status(301, b'Moved Permanently')
FOUND_302 = Status(302, b'Found')

# 4xx status codes
BAD_REQUEST_400 = Status(400, b'Bad Request')
UNAUTHORIZED_401 = Status(401, b'Unauthorized')
PAYMENT_REQUIRED_402 = Status(402, b'Payment Required')
FORBIDDEN_403 = Status(403, b'Forbidden')
NOT_FOUND_404 = Status(404, b'Not Found')
METHOD_NOT_ALLOWED_405 = Status(405, b'Method Not Allowed')
NOT_ACCEPTABLE_406 = Status(406, b'Not Acceptable')
PROXY_AUTH_REQUIRED_407 = Status(407, b'Proxy Authentication Required')
REQUEST_TIMEOUT_408 = Status(408, b'Request Timeout')
CONFLICT_409 = Status(409, b'Conflict')
GONE_410 = Status(410, b'Gone')
LENGTH_REQUIRED_411 = Status(411, b'Length Required')
PRECONDITION_FAILED_412 = Status(412, b'Precondition Failed')
PAYLOAD_TOO_LARGE_413 = Status(413, b'Payload Too Large')
URI_TOO_LONG_414 = Status(414, b'URI Too Long')
UNSUPPORTED_MEDIA_TYPE_415 = Status(415, b'Unsupported Media Type')
RANGE_NOT_SATISFIABLE_416 = Status(416, b'Range Not Satisfiable')
EXPECTATION_FAILED_417 = Status(417, b'Expectation Failed')
IM_A_TEAPOT_418 = Status(418, b'I\'m A Teapot')
MISDIRECTED_REQUEST_421 = Status(421, b'Misdirected Request')
UNPROCESSABLE_ENTITY_422 = Status(422, b'Unprocessable Entity')
LOCKED_423 = Status(423, b'Locked')
FAILED_DEPENDENCY_424 = Status(424, b'Failed Dependency')
UPGRADE_REQUIRED_426 = Status(426, b'Upgrade Required')
PRECONDITION_REQUIRED_428 = Status(428, b'Precondition Required')
TOO_MANY_REQUESTS_429 = Status(429, b'Too Many Requests')
REQUEST_HEADER_FIELDS_TOO_LARGE = Status(
    431, b'Request Header Fields Too Large'
)

# 5xx status codes
