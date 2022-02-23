# 12.1.1 调试手段，打印相关信息便于分析异常等
# 1、只能在开发时使用，print方法和pprint模块的pprint函数（打印JSON或dict格式数据时使用更好，会将键值结合打印）。
# 2、logging日志模块，收集线上数据时使用较好，还可以控制输出到文件还是控制台，并且可以通过级别控制输出。
# 3、pdb，可以跟踪程序的执行流程，观察问题所在，前2中无法做到；python -m pdb 文件名。
# 在pdb模式下，输入h可查看指令；n、s、c、l、ll、r、q等。pdb推荐使用，开始繁琐，之后会提高调试效率。兼容性好。

# 12.1.2 调优手段，优化代码，优化运行时间，提升性能。自带的功能模块。
# 1、timer，直接使用，或封装成装饰器执行更好；只能输入执行时间，无法看到执行细节和过程。
# 2、profile/cProfile,直接使用，或封装成类似装饰器执行更好；可查看细节、过程、执行多少次等。

# 使用第三方插件优化，提升性能。在虚拟环境安装
# 一、 12.2 使用django-debug-toolbar优化系统，专门做性能排查。
# 1、安装：pip install django-debug-toolbar;
# 2、配置develop， django-debug-toolbar只有在DEBUG为True时才会生效，只在开发和测试阶段使用。
# 3、配置urls。
# 4、解读数据，主要看cpu执行时间SQL执行情况中的最长时间等，详情见本书12.2.2
#
# 二、 12.2.3 配置第三方panel
# 1、djdt_flamegraph火焰图；安装：pip install djdt_flamegraph；配置develop；运行，观察分析。
# 2、pympler内存占用分析；安装，配置develop，运行，观察分析。
#
# 三、 12.2.4 line_profiler，行级性能分析插件。
# 安装，配置develop，运行，观察分析。可以看到每行代码的细节，过程详情。
#
# 四、 12.3 使用silk，更适合测试环境，多人访问，分析结果；django-debug-toolbar适合自己分析。
# 安装，配置develop，配置url，创建表：py manage.py migrate，运行，
# 随机访问几个页面模仿用户，再打开silk页面进行分析。
# 12.3.2 配置profiling，记录了装饰函数在执行时的耗时以及是否产生查询的情况，
# 通过silk_profile装饰器能够更明确地定位我们想要优化或者调试的函数。

# 调优思路：减少外部I/O，减少冗余的调用，优化耗时的逻辑。
