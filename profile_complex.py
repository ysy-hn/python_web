"""通常只在需要比cProfile.run()函数提供更精确的分析控制时才使用"""
import cProfile
import pstats
from io import StringIO


pr = cProfile.Profile()


def loop(count):
    result = []
    for i in range(count):
        result.append(i)


pr.enable()  # 开始收集分析数据
loop(10000)
pr.disable()  # 停止收集分析数据
# pr.create_stats()  # 停止收集性能数据并创建stats对象。
s = StringIO()  # 创建实例

# sortby = 'cumulative'
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# pstats.Stats,格式化展示cprofile的分析结果;sort_stats(sortby),对报告列表进行排序.
ps.print_stats()  # 创建一个Stats对象并将结果输出到stdout
print(s.getvalue())

# dump_stats(filename）将当前分析的结果写入文件（二进制格式）。
# runcall(func, *args, **kwargs): 收集被调用函数func的性能分析数据Stats类
# pstats模块提供的Stats类可以帮助我们读取和操作stats文件（二进制格式）


# 3. 关于Stats类
# Stats类源自pstats模块，使用前import pstats
# 主要用于格式化展示cprofile的分析结果；
# Stats类可以接受stats文件名，也可以直接接受cProfile.Profile对象作为数据源。
# strip_dirs(): 删除报告中所有函数文件名的路径信息
# dump_stats(filename): 把stats中的分析数据写入文件（效果同cProfile.Profile.dump_stats())
# sort_stats(*keys): 对报告列表进行排序，函数会依次按照传入的参数排序，关键词包括calls, cumtime等，具体参数参见官方文档；
# reverse_order(): 逆反当前的排序
# print_stats(*restrictions): 把信息打印到标准输出。*restrictions用于控制打印结果的形式,
# 例如(10, 1.0, ".*.py.*")表示打印所有py文件的信息的前10行结果。
