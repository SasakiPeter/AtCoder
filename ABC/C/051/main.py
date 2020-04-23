sx, sy, tx, ty = map(int, input().split())
h, w = (ty-sy), (tx-sx)
inner_route = "U"*h+"R"*w+"D"*h+"L"*w
outer_route = "L"+"U"*(h+1)+"R"*(w+1)+"D"
outer_route += "R"+"D"*(h+1)+"L"*(w+1)+"U"
print(inner_route+outer_route)
