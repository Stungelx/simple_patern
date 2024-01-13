from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
import sqlite3


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class UsersHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "users":
            with sqlite3.connect('db.sqlite3') as dbu:
                cursor = dbu.cursor()
                dtb1 = cursor.execute("""SELECT * FROM users""")
                result = dtb1.fetchall()
                return str([dict(zip(['id', 'name', 'email', 'gender', 'status', ], row)) for row in result])
        else:
            return super().handle(request)


class PostsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "posts":
            with sqlite3.connect('db.sqlite3') as dbu:
                cursor = dbu.cursor()
                dtb1 = cursor.execute("""SELECT * FROM posts""")
                result = dtb1.fetchall()
                return str([dict(zip(['id', 'name', 'email', 'gender', 'status', ], row)) for row in result])

        else:
            return super().handle(request)


class PasswordsHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "passwords":
            return f"Dog: I ate the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    for tabs in ["posts", "users", "passwords"]:
        print(f"\nClient: Who wants a {tabs}?")
        result = handler.handle(tabs)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {tabs} was left untouched.", end="")


if __name__ == "__main__":
    users = UsersHandler()
    posts = PostsHandler()
    dog = PasswordsHandler()

    users.set_next(posts).set_next(dog)
    print("Chain: Users > Passwords > Passwords")
    client_code(users)
    print("\n")

    print("Subchain: Passwords > Passwords")
    client_code(posts)
