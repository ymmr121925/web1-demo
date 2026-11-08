now = "10-18 12:00"
todos = [
    ("完成第二次作业", "10-20 23:59"),
    ("复习循环与条件判断", "10-17 14:30"),
    ("整理课堂笔记", "10-18 15:30"),
    ("看一遍讲义第二部分", "10-19 09:00"),
    ("准备演示用的数据", "10-16 20:00"),
    ("复习列表方法", "10-22 21:00"),
]
dones = [
    ("提交第一次作业", ["10-12 18:00", "10-12 16:40"]),
    ("背单词", ["10-16 22:00", "10-17 08:30"]),
    ("读完讲义第一部分", ["10-15 20:00", "10-15 19:30"]),
    ("整理错题", ["10-13 22:00", "10-14 09:10"]),
]

print("="*40)
print("第1题：访问数据")
print("="*40)
print("todos里第1条任务：", todos[0])
print("dones里第2条任务的完成时间：", dones[1][1][1])


print("="*40)
print("第2题：添加与删除")
print("="*40)
todos.append(("交作业截图", "10-25 18:00"))
del todos[2]
print("执行添加、删除之后，todos的任务条数：", len(todos))
print("当前 todos：", todos)


print("="*40)
print("第3题：判断任务状态")
print("="*40)
zongshu = len(todos)
guoqishu = 0
jinxingshu = 0
guoqimingdan = []

for a, b in todos:
    if b < now:
        state = "[已截止]"
        guoqishu += 1
        guoqimingdan.append(a)
        print(f"{a} 截止:{b} {state}")
    else:
        jinxingshu += 1

print("已截止的任务名称：", guoqimingdan)
print(f"汇总：总共有{zongshu}条任务，"
      f"已截止{guoqishu}条，"
      f"进行中{jinxingshu}条")

print("="*40)
print("第4题：任务完成，移入dones")
print("="*40)
move_list = []
for a, b in todos:
    if a == "复习循环与条件判断" or a == "完成第二次作业":
        move_list.append( (a, b) )
print(move_list)
# 搬到dones，同时从todos移除
for a, b in move_list:
    if a == "完成第二次作业":
        ft = "10-18 11:30"
    #dones:(任务名, [截止时间, 完成时间])
    else:
        ft = "10-18 09:00"
    dones.append( (a, [b, ft]) )
    todos.remove( (a, b) )
print("移动之后 todos: ", todos)
print("移动之后 dones: ", dones)

print("="*40)
print("第5题：给dones任务添加【按时/超时】标记")
print("="*40)
new_dones = []
for name, time_list in dones:
    ddl = time_list[0]
    ft = time_list[1]
    if ft <= ddl:
        tag = "按时"
    else:
        tag = "超时"
    new_item = (name, [ddl, ft, tag])
    new_dones.append(new_item)
print("新列表：",new_item)
dones = new_dones

for item in dones:
    print("新dones：",item)


print("="*40)
print("第6题：按完成时间从小到大排序（只用循环）")
print("="*40)
# 冒泡排序实现
temp = []
for item in dones:
    finish_t = item[1][1]
    temp.append( [finish_t, item] )
print("tepm：",temp)
n = len(temp)
for i in range(n - 1):
    for j in range(n - i - 1):
        if temp[j][0] > temp[j+1][0]:
            temp[j], temp[j+1] = temp[j+1], temp[j]

print("按完成时间升序结果：")
for one in temp:
    print(one(1))


