from typing import Optional


class AppController:
    def __init__(self, base_path: str):
        self.routes = dict()
        self._base_url = base_path

    def route(self, path: str, method: str, qualifier: Optional[str] = None):
        def _route(func: callable):
            path_ = f"{self._base_url}{path}"
            if path_ not in self.routes:
                self.routes[path_] = dict()
            self.routes[path_][method] = func, qualifier
            return func

        return _route

    def get(self, path: str = "", qualifier: Optional[str] = None):
        return self.route(path, "GET", qualifier)

    def post(self, path: str = "", qualifier: Optional[str] = None):
        return self.route(path, "POST", qualifier)

    def patch(self, path: str = "", qualifier: Optional[str] = None):
        return self.route(path, "PATCH", qualifier)

    def delete(self, path: str = "", qualifier: Optional[str] = None):
        return self.route(path, "DELETE", qualifier)

    def put(self, path: str = "", qualifier: Optional[str] = None):
        return self.route(path, "PUT", qualifier)
