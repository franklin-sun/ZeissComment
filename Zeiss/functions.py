import pymysql
import pandas as pd

class write_db:
    def __init__(self, name, context, date_time):
        # 我们这里需要多一步选择数据库
        db = pymysql.connect(
            host='localhost',  # 这里输入主机名称一般来说都是localhost
            user='root',  # 这里输入mysql用户名
            password='root',  # 这里输入密码
            port=3306,  # 这里输入端口号
            charset='utf8mb4',
            database='Zeiss'  # 这里选择数据库
        )

        # 创建一个游标对象
        cursor = db.cursor()

        # # 创建一个名为 user 的表
        # table_name = "ZeissComment"
        # sql = 'create table {} (id varchar(20) not null auto_increment, name varchar(20) not null, context varchar(9999), date_time datetime, primary key(id)'.format(table_name)
        # cursor.execute(sql)
        #
        # # 把创建的表显示出来
        # sql = 'show tables;'
        # cursor.execute(sql)
        # print("显示创建的表：", cursor.fetchall())
        #
        # # 显示表的结构
        # sql = 'desc {}'.format(table_name)
        # cursor.execute(sql)
        # print("显示表的结构：", cursor.fetchall())

        # 插入数据
        # id = int('1')
        sql = "INSERT INTO ZeissComment(name,context,date_time) VALUES (%s, %s, %s)"
        cursor.execute(sql,(name,context,date_time))
        db.commit()
        print('插入成功')

        cursor.close()
        db.close()  # 关闭数据库连接

class read_db():
    def __init__(self):
        # 我们这里需要多一步选择数据库
        db = pymysql.connect(
            host='localhost',  # 这里输入主机名称一般来说都是localhost
            user='root',  # 这里输入mysql用户名
            password='root',  # 这里输入密码
            port=3306,  # 这里输入端口号
            charset='utf8mb4',
            database='Zeiss'  # 这里选择数据库
        )

        # 创建一个游标对象
        cursor = db.cursor()

        sql = "select * from ZeissComment ORDER BY date_time desc;"
        df_data = pd.read_sql_query(sql, db)
        context = df_data['context'].tolist()
        string = ''
        comments = []
        for i in range(len(context)):
            if i < 3:
                string2 = df_data['name'][i] + ':' + df_data['context'][i]
                comments.append(string2)
                print(df_data['name'][i], ':', df_data['context'][i])
        for i in context:
            string = string + str(i)
            print(str(i))
        cursor.close()
        db.close()  # 关闭数据库连接
        self.text1 = string
        self.comments = comments
        print(string2)

    def get_string(self):
        text = self.text1
        return text

    def get_comments(self):
        comment1 = self.comments[0]
        comment2 = self.comments[1]
        comment3 = self.comments[2]
        return comment1, comment2, comment3

# import datetime
# date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(date_time)
# 微博
# write_db('可山海难平', '蔡司加油，带我去探索更远的未来', '2022-11-10 00:53:00')
# write_db('摄影宇小單', '蔡司将推动更多行业的发展与进步！', '2022-11-04 22:33:00')
# write_db('爱喝加冰气泡水', '蔡司好厉害', '2022-11-01 20:25:00')
# write_db('爱喝加冰气泡水', '蔡司的防蓝光镜对我们这些长期对着手机电脑的近视党太友好了', '2023-02-18 22:11:00')
# write_db('差评帝', '蔡司镜头表达有很多意想不到的高级感和炫酷玩法', '2023-05-19 11:05:00')
# # 公众号
# # 蔡司官方
# write_db('GYHIT', '蔡司，探幽入微、上天揽胜！', '2022-07-14 18:00:00')
# write_db('May Day', '从太空寄来的“明信片”，好美', '2022-07-14 18:00:00')
# write_db('Mia Chen', '宇宙星空无限，蔡司梦想卓越', '2022-07-14 18:00:00')
# write_db('Joanne乔安 境随心转', '蔡司，不仅是镜头', '2022-07-14 18:00:00')
# # 蔡司消费光学
# write_db('Carol', '这么轻，再也不担心出去玩回来脖子痛了', '2023-04-26 18:51:00')
# write_db('Coco 大珂', '目测又是一个帮儿子买来，爸爸先帮你试用系列', '2023-04-26 18:51:00')
# write_db('Connie Yu', '哇塞，这个望远镜看起来真的蛮小巧的，感觉带出去挺方便，可以考虑一下哈哈哈', '2023-04-26 18:51:00')
# write_db('Aki', '30这个我之前在国外官网看到了，一直很期待，现在中国也终于上市了，买买买！', '2023-04-26 18:51:00')
# # 蔡司显微镜
# write_db('夏夜微凉', '如果能有一台蔡司显微镜，我想用它来观察蝴蝶🦋的翅膀，我想知道蝴蝶翅膀上五彩斑斓的颜色是怎么产生的；我还想观察树叶，我想知道树叶从嫩绿变为深绿再变为金黄再变为火红的秘密；我还想观察一粒沙，想了解何为一沙一世界；我还想观察花蕊，了解雌雄花是如何孕育出植物宝宝！这个世界太奇妙了，需要我们用充满智慧的眼睛去发现更多的美好！', '2023-06-01 08:00:00')
# write_db('田美美 美好人生', '如果回到童年，我想用显微镜放大妈妈的爱。用显微镜看看妈妈的手，那是因为忙碌操持家务而变得粗糙的手；用显微镜看看妈妈炸的麻叶，菜籽油和面粉的混合使得食物散发出诱人的香；用显微镜看看妈妈为我抓的昆虫，让我的童年也有丰富多彩的回忆。', '2023-06-01 08:00:00')
# write_db('梅雨', '回到童年，如果拥有一台显微镜，当然是用来观察昆虫了，因为小时候最喜欢玩昆虫，长大后接触了许多电子产品，需要用显微镜观察芯片细节，也想拥有一台显微镜放在家里，给小朋友长见识', '2023-06-01 08:00:00')

db = read_db()
print(db.get_comments())