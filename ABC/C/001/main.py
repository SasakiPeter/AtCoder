deg, dis = map(int, input().split())
deg *= 10
# wd = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
#       'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
wd = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
      'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
wp = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326, 2000]

# wind_direction_range = []
# const = 2250
# x = 1125
# for d in wd:
#     wind_direction_range.append((d, (x, x+const)))
#     x += const


# print(wind_direction_range)

ans = [wd[(deg+1125)//2250 % 16]]
wind_power_range = []
L = 0
for p in wp:
    wind_power_range.append((L, p*6+3))
    L = p*6+3

# print(wind_power_range)
# ans = []

# for direction, rng in wind_direction_range:
#     L, R = rng
#     if L <= deg < R:
#         ans.append(direction)
#         break
# else:
#     ans.append('N')

for power, rng in enumerate(wind_power_range):
    L, R = rng
    if L <= dis < R:
        ans.append(power)
        break

if ans[-1] == 0:
    print('C', 0)
else:
    print(*ans)
