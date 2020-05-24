n, m = map(int, input().split())
minutes = n*60+m
h_deg = minutes/2 % 360
m_deg = minutes*6 % 360

deg = abs(h_deg - m_deg)
if 180 < deg:
    deg = 360-deg
print(deg)
