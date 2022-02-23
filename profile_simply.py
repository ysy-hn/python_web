"""如果没有给出文件名，则该函数创建一个Stats 实例并打印一个简单的性能分析报告。如果指定了排序方式，此Stats实例以指定方式排序。"""
import cProfile


def loop(count):
    result = []
    for i in range(count):
        result.append(i)


cProfile.run('loop(10000)', filename='profile.out', sort='cumulative')
# filename:指定文件输出结果；默认输出到控制台；sort：以某种排列排序
