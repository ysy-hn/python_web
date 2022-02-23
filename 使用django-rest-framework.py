# 1、前后端不分离[客户端看到的内容和所有界面效果都是由服务端提供出来的。]
# 2、前后端分离[把前端的界面效果(html，css，js分离到另一个服务端，python服务端只需要返回数据即可]。前端形成一个独立的网站，服务端构成一个独立的网站

# API：如果我们把前端页面看作是一种用于展示的客户端，那么 API 就是为客户端提供数据、操作数据的接口。
# 目前市面上大部分公司开发人员使用的接口服务架构主要有：restful、rpc、soap。

# 什么是RESTful API？
# 将所有的事物抽象为资源，资源对应唯一的标识。RESTful为表现层状态转移，是一种以资源为中心的web软件架构风格。
# 资源：使用URL指向一个实体。
# 表现层：资源的表现形式；比如图片、HTML文本等。
# 状态转移：使用GET/ POST/ PUT/ DELETE等HTTP动词操作资源，实现资源状态转变。
# RESTful风格的API即为RESTful API。通过GET/ POST/ PUT/ DELETE来获取/新建/更新/删除资源。
# 一般使用JSON格式返回数据。大多数web框架都有相应的插件支持RESTful API。

# 序列化：比如在django中获取到的数据默认是模型对象，但是模型对象数据无法直接提供给前端或别的平台使用，
# 所以需要把数据进行序列化，变成字符串或者json数据，提供给别人。
# 反序列化：比如前端js提供过来的json数据，对于python而言就是字符串，我们需要进行反序列化换成模型类对象，
# 这样才能把数据保存到数据库中。两者都是数据转换格式。
#
# 安装：
# pip install djangorestframework  安装Django Rest framework
# pip install markdown       # 为browsable API 提供Markdown（标记）支持。
# pip install django-filter  # Filtering（过滤）支持。

# 在项目中如果使用rest_framework框架实现API接口，主要有以下三个步骤：
# 1、将请求的数据（如JSON格式）转换为模型类对象；
# 2、通过模型类对象进行数据库操作，完成客户端请求的增删查改；
# 3、将模型类对象转换为响应的数据（如JSON格式）。
#

