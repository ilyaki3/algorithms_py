"""
Написать код для задачи: "Обработка сетевых пакетов", условие здесь:
https://stepik.org/media/attachments/lesson/41233/statements.pdf
"""

from collections import deque


def buffer():
    size, n = map(int, input().split())
    queue = deque()

    for _ in range(n):
        arrival, duration = map(int, input().split())

        if len(queue) == 0:
            print(arrival)
            arrival += duration
            queue.appendleft(arrival)

        elif queue[-1] <= arrival:
            arrival = max(queue[0], arrival)
            print(arrival)
            queue.pop()
            arrival += duration
            queue.appendleft(arrival)

        elif len(queue) >= size:
            print(-1)

        else:
            arrival = max(queue[0], arrival)
            print(arrival)
            arrival += duration
            queue.appendleft(arrival)


if __name__ == '__main__':
    buffer()
