# 本数　1e+9
n, m = map(int, input().split())
# 所要時間
x, y = map(int, input().split())
# 時刻表
a = sorted(map(int, input().split()), reverse=True)
b = sorted(map(int, input().split()), reverse=True)

# 時刻表から、一番小さい値を順番にのぞいていく必要がある。
# 頭かな抜くとO(n)になるから、降順ソートして、お尻からpopする

# 最初から時刻表に所要時間を足すとどうなる？

ans = time = 0

while True:
    while a:
        departure_time = a.pop()
        if time <= departure_time:
            time = departure_time + x
            break
    else:
        break

    while b:
        departure_time = b.pop()
        if time <= departure_time:
            time = departure_time + y
            ans += 1
            break
    else:
        break

print(ans)


# for_b = True

# while True:
#     if for_b:
#         while a:
#             departure_time = a.pop()
#             if time <= departure_time:
#                 time = departure_time + x
#                 break
#         else:
#             time = -1

#         for_b = False
#     else:
#         while b:
#             departure_time = b.pop()
#             if time <= departure_time:
#                 time = departure_time + y
#                 break
#         else:
#             time = -1

#         if time != -1:
#             ans += 1
#         for_b = True
#     if time == -1:
#         break


# copyはO(n)
# def leave(time_table, cost, time):
#     time_table = time_table.copy()
#     while time_table:
#         departure_time = time_table.pop()
#         if time <= departure_time:
#             time = departure_time + cost
#             break
#     else:
#         time = -1
#     return time_table, time
