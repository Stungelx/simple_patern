import httpx
import sqlite3


class Target:

    def all_users(self) -> list:
        with sqlite3.connect('db.sqlite3') as dbu:
            cursor = dbu.cursor()
            dtb1 = cursor.execute("""SELECT * FROM users""")
            result = dtb1.fetchall()
            return [dict(zip(['id', 'name', 'email', 'gender', 'status',], row)) for row in result]


class Adaptee:
      def url_database(self):
        url = "https://gorest.co.in/public/v2/users"
        return url


class Adapter(Target, Adaptee):
    def all_users(self) -> list:
        al_us = []
        response = httpx.get(self.url_database())
        if response.status_code == 200:
            data = response.json()
            for user_data in data:
                al_us.append(user_data)
        return al_us


def client_code(target: "Target") -> None:
    print(target.all_users())


print("Client: I can work just fine with the Target objects:")
target = Target()
print("Target: ", end='')
print(client_code(target))
print("\n")

adaptee = Adaptee()
print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
print(f"Adaptee: {adaptee.url_database()}", end="\n\n")


print("Client: But I can work with it via the Adapter:")
print("Adapter: ", end='')
adapter = Adapter()
client_code(adapter)
