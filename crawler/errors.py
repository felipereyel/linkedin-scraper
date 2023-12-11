class LoginError(Exception):
    def __init__(self) -> None:
        super().__init__("Login failed")


class SearchError(Exception):
    def __init__(self) -> None:
        super().__init__("Search failed")


class EmployeeError(Exception):
    def __init__(self) -> None:
        super().__init__("Employee count failed")
