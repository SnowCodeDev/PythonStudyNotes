# 初识 turtle 库

`turtle`（海龟）库是Python的标准库之一，它提供了一种非常直观的方式来学习编程和图形绘制。你可以把它想象成在画布上控制一只"海龟"，通过给它下达前进、转弯等指令，让它爬行并留下轨迹，从而绘制出图形。

## 1. 创建你的画布和海龟

在使用海龟绘图之前，通常需要初始化一个"海龟"对象。我们常常给这个对象起一个简短的名字，比如 `t`。

```python
import turtle

# 创建画布窗口
window = turtle.Screen()
# 创建一只海龟，并把它赋给变量 t
t = turtle.Turtle()
```

> [!IMPORTANT]
> **理解对象**
> 这里的 `t = turtle.Turtle()` 意味着我们创建了一个独立的、具体的"海龟"实例。之后所有的绘图命令（如前进、转向）都将由 `t` 来执行。你可以创建多只海龟，让它们画不同的东西。

## 2. 基础移动命令

海龟有四个基本的移动命令，它们是绘图的基础：

```python
t.forward(distance)   # 向前移动指定像素距离
t.backward(distance)  # 向后移动指定像素距离
t.right(angle)        # 向右（顺时针）旋转指定角度
t.left(angle)         # 向左（逆时针）旋转指定角度
```

### 示例：画一条线并转弯

```python
import turtle
t = turtle.Turtle()

t.forward(100)  # 向前走100像素，画一条长100的线
t.right(90)     # 向右转90度
t.forward(50)   # 再向前走50像素
```

## 3. 使用循环画一个六边形

六边形的每个外角是60度。所以画法可以是：前进一段距离 → 右转60度 → 重复6次。

```python
import turtle

t = turtle.Turtle()
t.shape("turtle")  # 让海龟显示为乌龟形状，更有趣！

# 画一个六边形
for _ in range(6):
    t.forward(100)  # 前进100像素
    t.right(60)     # 右转60度

# 保持窗口打开，直到点击关闭
turtle.done()
```

> [!IMPORTANT]
> **循环的作用**
> `for _ in range(6):` 这行代码会让缩进内的两条命令重复执行6次。这是编程中"自动化重复工作"的典型例子。

> [!TIP]
> **尝试修改**
> - 把 `forward(100)` 中的100改成其他数字，看看六边形大小如何变化
> - 把 `right(60)` 中的60改成90，看看会画出什么形状（正方形！）
> - 在循环前添加 `t.color("red")` 可以让海龟画出红色的线

## 4. 完整示例代码

这里是一个完整的示例，包含一些美化设置：

```python
import turtle

# 设置画布
window = turtle.Screen()
window.title("我的第一个海龟图形")
window.bgcolor("lightblue")

# 创建海龟
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen")
t.pensize(3)  # 设置画笔粗细
t.speed(5)    # 设置绘制速度（1-10，数字越大越快）

# 画六边形
for i in range(6):
    t.forward(100)
    t.right(60)

# 画完回到中心点并显示文字
t.penup()
t.goto(0, -50)
t.color("black")
t.write("六边形完成！", align="center", font=("Arial", 12, "normal"))

# 保持窗口打开
turtle.done()
```

> [!NOTE]
> **关键点总结**
> 1. `import turtle` - 导入库
> 2. `t = turtle.Turtle()` - 创建海龟对象
> 3. `t.forward()` / `t.right()` - 基本移动命令
> 4. `for ... in range():` - 使用循环重复动作
> 5. `turtle.done()` - 保持窗口打开

现在你可以复制上面的完整代码，保存为 `.py` 文件（如 `turtle_demo.py`），然后运行它看看效果！
