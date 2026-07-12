from src.logger import (
    log_success,
    log_failure
)


log_success(
    "rahul@example.com"
)


log_failure(
    "anita@example.com",
    "SMTP connection failed"
)


print(
    "Logging test completed"
)
