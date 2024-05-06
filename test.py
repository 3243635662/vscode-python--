c=9.88
s=7.66
print("三角形的周长是{0:.1f}".format(c)+'\n'+ "三角形的面积是:{0:.1f}".format(s))
#沉浸式体验vscode的强大
#全局和局部变量以及作用域
#在函数体中默认情况下只能改变形参的值，不能改变实参的值，如果需要改变实参的值，需要在函数体中用形参的名字来指定实参，并用赋值运算符来修改实参的值。
#  一： 利用return语句在函数调用结束后将返回值赋值给实参
#  二   利用可变对象也能在函数内改变实参的值，如列表、字典等。
#  三   利用global和nonlocal关键字来修改全局变量和局部变量的值。
# 举例
# 一
def fun_1(x):
    return x*x
x=5
x=fun_1(x)
print(x)  #结果为25
# 二
def fun_2(my_list,new_item):
    my_list.append(new_item)
    return my_list 
my_list=[1,2,3]
new_item=4
my_list=fun_2(my_list,new_item) # my_list被修改为[1,2,3,4]
print(my_list)
# 三
a=1
b=2
print(a,b)
def fun_3(a):
    global b #全局变量b声明
    b=a
    a=0
fun_3(a)
print(a,b)  # global关键字使得全局变量b的值被改变，而a的值没有改变
# 四
#通过nonlocal关键字可以修改嵌套函数的局部变量的值。
def fun_4():
    a=1
    b=2
    print(f"在fun_4函数中a的值为{a},b的值为{b}")
    def fun_5():
        nonlocal a # 声明a为nonlocal变量
        a=3
        b=4
        print(f"在fun_5函数中a的值为{a},b的值为{b}")
    fun_5() # 记得在大函数里面调用小函数，否则a的值不会被修改
fun_4() # 共有两条打印语句