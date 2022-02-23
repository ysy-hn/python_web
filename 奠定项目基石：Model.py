# 5.1 创建项目即配置
# 通用文件结构解释：
# changelog.md：记录项目变更，发布版本的更新；
# license：如果是开源项目，增加这个文件来声明版权；
# readme：介绍项目信息；
# requirements.txt：项目的依赖库；编写：将每个依赖库的名称和版本写入其中；
# 使用：创建虚拟环境并激活，pip install -r requirements.tst,会将文件中的依赖库全部安装。

# 开始django项目：
# 1、创建虚拟环境并激活，安装django（创建：py -m venv project-env;
# 激活：project-env\Scripts\activate；安装：pip install django；停止：deactivate）
# 2、django-admin startproject 项目名：创建django源码项目；
# 还可以创建同级的desc目录，存储项目接口、第三方参考、开发文档等；其它人接手时更便捷。
# 3、拆分并配置settings方便以后维护，注意环境变量的修改，manage和wsgi文件的修改。
# 4、配置Git跟踪项目。开始进行项目代码的编写。

# 5.2 编写model层代码，先梳理模型关系图，可使用UML、ER图、思维导图来分析。
# 创建项目app，py manage.py startapp app名;进行model代码编写。
# Meta类属性，配置model的属性，每个model都会定义，展示名称：verbose_name。
# 每个field相当于数据库中的字段，model相当于MySQL的表。
# 模型代码编写好后需要添加到settings中；注意添加顺序。注意每次对model层的修改都需要迁移数据：
# py manage.py makemigrations,生成迁移规则和文件夹；py manage.py migrate,进行迁移。

# 5.3.1 ORM 的基本概念,“对象关系映射”,把我们定义的对象（类）映射到对应的数据库的表上.
# ORM 就是代码（软件）层面对于数据库表和关系一种抽象。Django的Model就是ORM的一个具体实现。
# 一个Model也就对应关系数据库中的一张表，而对于有关联关系的Model，比如用到了ForeignKey的Mode，就是通过外键关联的表。

# 5.3.2 常用字段类型；5.3.3 参数，详情见本书5.3.2和5.3.3.
# 5.4.1 Queryset的概念，本质是一个懒加载的对象，调用时还是queryset对象，只有在使用时才会执行查询。
# 链式调用：执行一个对象中的方法之后还是这个对象。
# 5.4.2 常用的queryset接口，详情见5.4.2。
# 5.4.3 进阶接口，详情见5.4.3.
# 5.4.4 常用的字段查询，详情见4.5.4.
# 5.4.5 进阶查询，详情见5.4.5.
# F：执行数据库层面的计算，避免出现竞争状态（多线程只+1），比如处理访问量；
# Q
# Count：聚合查询，比如某个分类下有多少文章；annotate：增加属性；
# Sum：合计，比如统计访问量多少。aggregate:直接计算结果。

