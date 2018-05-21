from collections import namedtuple

Status = namedtuple('Status', ['code', 'reason'])

# 2xx status codes
HTTP_200_OK = Status(200, b'OK')
HTTP_201_CREATED = Status(201, b'Created')

# 3xx status codes
HTTP_300_MULTIPLE_CHOICES = Status(300, b'Multiple Choices')
HTTP_301_MOVED_PERMANENTLY = Status(301, b'Moved Permanently')
HTTP_302_FOUND = Status(302, b'Found')

# 4xx status codes
HTTP_400_BAD_REQUEST = Status(400, b'Bad Request')
HTTP_401_UNAUTHORIZED = Status(401, b'Unauthorized')
HTTP_402_PAYMENT_REQUIRED = Status(402, b'Payment Required')
HTTP_403_FORBIDDEN = Status(403, b'Forbidden')
HTTP_404_NOT_FOUND = Status(404, b'Not Found')
HTTP_405_METHOD_NOT_ALLOWED = Status(405, b'Method Not Allowed')
HTTP_406_NOT_ACCEPTABLE = Status(406, b'Not Acceptable')
HTTP_407_PROXY_AUTH_REQUIRED = Status(407, b'Proxy Authentication Required')
HTTP_408_REQUEST_TIMEOUT = Status(408, b'Request Timeout')
HTTP_409_CONFLICT = Status(409, b'Conflict')
HTTP_410_GONE = Status(410, b'Gone')
HTTP_411_LENGTH_REQUIRED = Status(411, b'Length Required')
HTTP_412_PRECONDITION_FAILED = Status(412, b'Precondition Failed')
HTTP_413_PAYLOAD_TOO_LARGE = Status(413, b'Payload Too Large')
HTTP_414_URI_TOO_LONG = Status(414, b'URI Too Long')
HTTP_415_UNSUPPORTED_MEDIA_TYPE = Status(415, b'Unsupported Media Type')
HTTP_416_RANGE_NOT_SATISFIABLE = Status(416, b'Range Not Satisfiable')
HTTP_417_EXPECTATION_FAILED = Status(417, b'Expectation Failed')
HTTP_418_IM_A_TEAPOT = Status(418, b'I\'m A Teapot')
HTTP_421_MISDIRECTED_REQUEST = Status(421, b'Misdirected Request')
HTTP_422_UNPROCESSABLE_ENTITY = Status(422, b'Unprocessable Entity')
HTTP_423_LOCKED = Status(423, b'Locked')
HTTP_424_FAILED_DEPENDENCY = Status(424, b'Failed Dependency')
HTTP_426_UPGRADE_REQUIRED = Status(426, b'Upgrade Required')
HTTP_428_PRECONDITION_REQUIRED = Status(428, b'Precondition Required')
HTTP_429_TOO_MANY_REQUESTS = Status(429, b'Too Many Requests')
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = Status(
    431, b'Request Header Fields Too Large'
)
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = Status(
    451, b'Unavailable For Legal Reasons'
)

# 5xx status codes
