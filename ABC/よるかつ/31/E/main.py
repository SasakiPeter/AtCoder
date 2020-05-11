# EDPCのdequeを理解してから、この問題をまた見たい


# この方法実装厳しすぎる
# # 倍の長さにして、尺取っていく
# # 尺の長さはn以下でないといけない
# # さらに、
# n, k = map(int, input().split())
# V = list(map(int, input().split()))
# VV = V+V


# # 尺はコストの合計がKまで伸ばせる
# # Kに余裕がある時は、負の値は２コストかけていいけど、
# # 余裕が無くなったら、負の値のコストを１で計算
# # 価値は、取得したものから、負の値
# R = 0
# negative = []
# value = 0
# for L in range(2*n):

#   #
#   while R<2*n and R-L<=k:
#     value += VV[R]
#     R+=1
