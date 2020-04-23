S = list(input())
T = input()
ls = []
for i in range(len(S)-len(T)+1):
    for j in range(len(T)):
        if S[i+j] != T[j] and S[i+j] != "?":
            break
    else:
        ls.append(i)

if ls:
    for j in range(len(T)):
        S[ls[-1]+j] = T[j]
    print("".join(S).replace("?", "a"))
else:
    print("UNRESTORABLE")
