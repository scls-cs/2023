---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
rise:
  start_slideshow_at: beginning

kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 多分支语句 #

:::{note}
这一节是基于 [*Jupyter Notebook*]来生成，你可以点击右上角的Live Code进入编程模式。
:::

[*Jupyter Notebook*]: https://jupyter.org/about

## elif ##

if-else又被称为双分支语句。其实Python还可以支持多分支语句。

多分支语句的语法如下：
```python
if(cond1):
    A
elif(cond2):
    B
elif(cond3):
    C
...
else:
    X
```
如果cond1成立，就执行A；如果cond1不成立，就再看cond2是否成立。如果cond2成立，那么执行B；否则再看看cond3是否成立...如果所有条件都不成立，那么就执行X。

```{code-cell} python3
grade = 75
if(grade >= 90):
    print("A")
elif(grade >= 80):
    print("B")
elif(grade >= 70):
    print("C")
elif(grade >= 60):
    print("D")
else:
    print("Class Failed!")
```

```{note}
多分支语句和双分支语句一样，有且只有一个分支会被执行。
```

## if和elif
对于很多初学者来说，会误以为elif可以用多个if语句来代替。例如上面的程序可以写成：
```{code-cell} python3
if(grade >= 90):
    print("A")
if(grade >= 80):
    print("B")
if(grade >=70):
    print("C")
if(grade >= 60):
    print("D")
```

多分支语句中，只有一个条件能够成立（否则执行else分支）。

在多个if语句中，程序会检查每一个条件，只要条件成立就会执行对应的语句。

（如果你考了95分，程序会打印”A“，“B”，“C”，“D”四个结果，因为每一个条件都成立！）

## if语句的嵌套 ##

if, else和elif可以嵌套起来一起使用，称为条件嵌套(nested condition)。

条件嵌套的关键是缩进，缩进决定了不同分支的逻辑层次。

```{code-cell} python3
def checkBMI(bmi):
  if(bmi < 18.5):
      print("Too thin")
  else:
      if(bmi < 25):
          print("Fit")
      elif(bmi < 30):
          print("Overweight")
      elif(bmi < 40):
          print("Obesity")
      else:
          print("Go to see a doctor right now.")
```
上面这段代码有两个条件结构：第一个条件结构包含if-else两个分支；第二个条件结构嵌套在else分支里，包含四个分支。

## Exercise ##

Ex0. 程序运行后，a，b，x，y的值分别是什么？
```python
x = 7
y = 4
a = False
b = False
if (x > y):
    if (x % y <= 2):
        a = True
        x = x + y
    elif (x/y < 2):
        x = x - y
        b = True
    else:
        x = y + 1
if (x < y):
    if (y % x >= 3):
        b = True
        x = x - y;
    else:
        x = x + y
```

Ex1. 某地按照阶梯电价计算电费，计算规则如下：
```{list-table}
   :widths: 25 25  50
   :header-rows: 1

   * - 类别
     - 用电量
     - 电价标准
   * - 一档
     - 1-240（含）
     - 0.48
   * - 二档
     - 241-400（含）
     - 0.54
   * - 三档
     - 400以上
     - 0.79
```
请编写函数来实现这一功能。

```{code-cell} python3
def getBill(degrees):
    cost = 0
    if(degrees <= 240):
        cost = degrees*0.48
    #add code here
    
    return cost


print(getBill(200)) #96.0
print(getBill(350)) #174.6 
print(getBill(500)) #280.6
```
ex2. Your cell phone rings. Return true if you should answer it. Normally you answer, except in the morning you only answer if it is your mom calling. In all cases, if you are asleep, you do not answer.

answerCell(False, False, False) → True

answerCell(False, False, True) → False

answerCell(True, False, False) → False

```{code-cell} python3
def answerCell(isMorning, isMom, isAsleep):
   #add code here
   return True


print(answerCell(False, False, False)) # True
print(answerCell(False, False, True)) # False
print(answerCell(True, False, False)) # False
```

## 作业 ##
[Problem Set 7](hw7.md)
