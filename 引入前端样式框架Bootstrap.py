# jumbotron：超大屏幕，使用大块内容展示重要内容，例如标题等。
# card：卡片组件，以卡片的方式来组织内容的展示。

# col-？排版的简介
# .col-xs- 超小屏幕 手机 (<768px)
# .col-sm- 小屏幕 平板 (≥768px)
# .col-md- 中等屏幕 桌面显示器 (≥992px)
# .col-lg- 大屏幕 大桌面显示器 (≥1200px)
# 1、col-列；
# 2、xs-maxsmall，超小；sm-small，小；md-medium，中等；lg-large，大；
# 3、-*表示占列，即占自动每行row分12列栅格系统比；
# 4、不管在哪种屏幕上，栅格系统都会自动的每行row（排）分12列 col-xs-*和col-sm-*
# 和col-md-*后面跟的参数表示在当前的屏幕中 每个div所占列数。
# 例如 <div class="col-xs-6 col-md-3"> 这个div在屏幕中占的位置是：
# .col-xs-6 在超小屏幕中占6列 也就是屏幕的一半（12/6列=2个div） ，
# .col-md-3 在中单屏幕中占3列也就是1/4（12/3列=4个div）。
# div：在html中划分区域。
# 5、混用案例：
# < div class ="col-xs-12 col-sm-9 col-md-6 col-lg-3" >< / div >
# 当屏幕尺寸：小于 768px 的时候，用 col-xs-12 类对应的样式；
# 在 768px 到 992px 之间的时候，用 col-sm-9 类对应的样式；
# 在 992px 到 1200px 之间的时候，用 col-md-6 类对应的样式；
# 大于 1200px 的时候，用 col-lg-3 类对应的样式。

# nav导航的简介
# .justify-content-center：水平居中；<nav class="nav justify-content-center">
# .justify-content-end右对齐；不设置时，默认左对齐。
# lex-column：垂直排列；<nav class="nav flex-column">；
# dropdown：带下拉列表的标签页；
#