import time
import random
from typing import List, Tuple

"""
Для хранения сессий пользователей на сервере используется структура, состоящая из наборов (username, role, last_activity_time)
username - имя пользователя
role — роль пользователя
last_activity_time — время последнего действия на сервере.
Необходимо решить оптимальным образом две задачи:
1) Определение роли пользователя по его username
2) Хранить надо сесси для которых последнее действие пользователя было не позже 60 минут, остальные удалять. Т. е. нужна оптимальная процедура поиска устаревших сессий.
Написать программу реализующую хранение (использовать 20 тестовых данных), определение роли, поиск и удаление просроченной сессии.

Note: Все алгоритмы должны быть реализованы самостоятельно, встроенные методы сортировки и поиска не использовать, 
свойства уникальности элементов set не использовать, можно использовать получение элемента из списка или кортежа по его индексу,
 встроенное получение значения словаря по ключу не использовать. Сравнение строк производить посимвольно, лексикографически.
"""

class UserManager:
    def __init__(self):
        self.sessions = []

    def generateSessions(self, numberOfSessions: int = 20) -> None:
        ROLES = ["ADMIN", "USER", "GUEST"]

        for i in range(numberOfSessions):
            username = f"user_{i+1}"
            role = random.choice(ROLES)  
            last_activity_time = time.time() - random.uniform(0, 120 * 60)

            self.sessions.append((username, role, last_activity_time))

    def getRoleByUsername(self, username: str) -> None:
        def compareStrings(a: str, b: str) -> int:
            lenA = len(a)
            lenB = len(b)
            minLen = min(lenA, lenB)
            for i in range(minLen):
                if a[i] < b[i]:
                    return -1
                elif a[i] > b[i]:
                    return 1

            if lenA < lenB:
                return -1
            elif lenA > lenB:
                return 1
            else:
                return 0

        for session in self.sessions:
            name = session[0]
            if compareStrings(name, username) == 0:
                role = session[1]

                print(f"Роль пользователя {username}: {role}")
                print()

    def removeExpiredSessions(self) -> None: 
        currentTime = time.time()
        activeSessions = []

        for session in self.sessions:
            last_activity_time = session[2]
            if currentTime - last_activity_time <= (60 * 60):
                activeSessions.append(session)

        self.sessions = activeSessions

    def printActiveSessions(self) -> None:
        if self.sessions:
            print("Активные сессии:")
            for session in self.sessions:
                username, role, last_activity_time = session
                print(f"Имя пользователя: {username}, Роль: {role}, Время последнего действия (в секундах): {last_activity_time}")
            print()
            return
        
        print("На данный момент нет активных сессий")
        print()

def main() -> None:
    userManager = UserManager()

    userManager.generateSessions()
    userManager.printActiveSessions()

    randomUser = random.choice(userManager.sessions)[0]
    userManager.getRole(randomUser)

    userManager.removeExpiredSessions()
    userManager.printActiveSessions()

if __name__ == "__main__":
    main()
