# 6.1.1 创建blog的管理后台
# 创建超级账号：py manage.py createsuperuser.
# 重写ModelAdmin的save_model方法，自动获取当前用户信息并设置为作者。
# 2.编写Post的管理后台，可以自定义增加字段，需要自定义增加函数方法并使用short_description="展示内容"；
# 3.model的__str__方法，每个model都需要。
# 6.2.1 定义list页面，修改用户权限，只能看到自己创建的文章，使用过滤器；关于数据过滤的部分，
# 只需要找到数据源在哪，就是Queryset在那生成，然后过滤。SimpleListFilter类的方法重写。
# 6.2.2 编辑页面配置，fields限定展示字段和顺序，fieldsets控制页面布局，classes给配置板块增加CSS属性。
# 6.2.3 自定义静态资源引入，在PostAdmin下，增加属性。
# 6.2.4 自定义form，model是对数据库中字段的抽象，form是对用户输入以及model中要展示数据的抽象。
# 6.2.5 在同一页面编辑关联数据，使用inline admin方很好。
# 6.2.6 定制site，分离用户管理和用户业务使用。
# 6.2.7 admin权限逻辑和SSO登录。
# 6.3.1 抽象author基类或其它容易用到的类并抽象基类，对于所有app都需要用到的放在主流程中。
# 6.4 记录操作日志，LogEntry模块或ModelAdmin中的log_addition和log_change方法都可使用。
#
#
#
