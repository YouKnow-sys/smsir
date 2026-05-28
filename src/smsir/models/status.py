from enum import IntEnum


class StatusCode(IntEnum):
    SUCCESS = 1
    ERROR = 0
    INVALID_API_KEY = 10
    DISABLED_API_KEY = 11
    IP_RESTRICTED_API_KEY = 12
    DISABLED_ACCOUNT = 13
    SUSPENDED_ACCOUNT = 14
    PLAN_UPGRADE_REQUIRED = 15
    INVALID_PARAMETER_VALUE = 16
    RATE_LIMITED = 20
    INVALID_LINE_NUMBER = 101
    INSUFFICIENT_CREDIT = 102
    EMPTY_MESSAGE_TEXT = 103
    INVALID_MOBILE = 104
    TOO_MANY_MOBILES = 105
    TOO_MANY_TEXTS = 106
    EMPTY_MOBILE_LIST = 107
    EMPTY_TEXT_LIST = 108
    INVALID_SEND_TIME = 109
    MISMATCHED_COUNTS = 110
    SEND_NOT_FOUND = 111
    RECORD_NOT_FOUND = 112
    TEMPLATE_NOT_FOUND = 113
    PARAMETER_VALUE_TOO_LONG = 114
    BLACKLISTED_MOBILES = 115
    EMPTY_PARAMETER_NAME = 116
    MESSAGE_NOT_APPROVED = 117
    TOO_MANY_MESSAGES = 118
    CUSTOM_TEMPLATE_REQUIRES_UPGRADE = 119
    SENDER_LINE_NEEDS_ACTIVATION = 123
    OTP_ONLY_MODE = 124


STATUS_MESSAGES: dict[int, str] = {
    StatusCode.ERROR: "Request failed",
    StatusCode.INVALID_API_KEY: "Invalid API key",
    StatusCode.DISABLED_API_KEY: "API key is disabled",
    StatusCode.IP_RESTRICTED_API_KEY: "API key is restricted to specific IPs",
    StatusCode.DISABLED_ACCOUNT: "Account is disabled",
    StatusCode.SUSPENDED_ACCOUNT: "Account is suspended",
    StatusCode.PLAN_UPGRADE_REQUIRED: "Plan upgrade required to use web service",
    StatusCode.INVALID_PARAMETER_VALUE: "Invalid parameter value",
    StatusCode.RATE_LIMITED: "Rate limit exceeded",
    StatusCode.INVALID_LINE_NUMBER: "Invalid line number",
    StatusCode.INSUFFICIENT_CREDIT: "Insufficient credit",
    StatusCode.EMPTY_MESSAGE_TEXT: "Empty message text(s)",
    StatusCode.INVALID_MOBILE: "Invalid mobile number(s)",
    StatusCode.TOO_MANY_MOBILES: "Too many mobile numbers (max 100)",
    StatusCode.TOO_MANY_TEXTS: "Too many message texts (max 100)",
    StatusCode.EMPTY_MOBILE_LIST: "Empty mobile list",
    StatusCode.EMPTY_TEXT_LIST: "Empty text list",
    StatusCode.INVALID_SEND_TIME: "Invalid send time",
    StatusCode.MISMATCHED_COUNTS: "Mobile and text counts don't match",
    StatusCode.SEND_NOT_FOUND: "No send found with this ID",
    StatusCode.RECORD_NOT_FOUND: "Record not found for deletion",
    StatusCode.TEMPLATE_NOT_FOUND: "Template not found",
    StatusCode.PARAMETER_VALUE_TOO_LONG: "Parameter value exceeds 25 characters",
    StatusCode.BLACKLISTED_MOBILES: "Mobile number(s) are blacklisted",
    StatusCode.EMPTY_PARAMETER_NAME: "Parameter name is empty",
    StatusCode.MESSAGE_NOT_APPROVED: "Message text not approved",
    StatusCode.TOO_MANY_MESSAGES: "Too many messages",
    StatusCode.CUSTOM_TEMPLATE_REQUIRES_UPGRADE: "Custom templates require plan upgrade",
    StatusCode.SENDER_LINE_NEEDS_ACTIVATION: "Sender line needs activation",
    StatusCode.OTP_ONLY_MODE: "Only OTP messages allowed and template is not OTP",
}


class DeliveryState(IntEnum):
    DELIVERED = 1
    NOT_DELIVERED_TO_PHONE = 2
    DELIVERED_TO_TELECOM = 3
    NOT_DELIVERED_TO_TELECOM = 4
    DELIVERED_TO_OPERATOR = 5
    FAILED = 6
    BLACKLISTED = 7
    UNKNOWN = 8
