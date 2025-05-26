result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)
print(result)



# 画出流程图
def team(work):
    return t(work) - 1
def dream(work, s):
    if work(s-2):
        t = not s
    return not t
work, t = 3, abs
team = dream(team, work + 1) and t