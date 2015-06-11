SELECT `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/news.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30


sources = ['http://www.zaobao.com/ssi/rss/news.xml',
           'http://www.zaobao.com/ssi/rss/zg.xml',
           'http://www.zaobao.com/ssi/rss/gj.xml',
           'http://www.zaobao.com/ssi/rss/yx.xml',
           'http://www.zaobao.com/ssi/rss/yl.xml',
           'http://www.zaobao.com/ssi/rss/cz.xml',
           'http://www.zaobao.com/ssi/rss/ty.xml',
           'http://www.zaobao.com/ssi/rss/wencui.xml']

sql_select = "SELECT %s FROM `zaobao_rss` WHERE `zb_rss_source` = '%s' ORDER BY `zb_item_pubdate` DESC LIMIT 30"
sql_format = "`zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description`"

sql = []
for i in range(len(sources)):
    sql.append(sql_select % (sql_format, sources[i]))

sqls = '(%s) union all (%s) union all (%s) union all (%s) union all (%s) union all (%s) union all (%s) union all (%s)' % tuple(sql)

print sqls
a = ['a','b','c','d']
content = ''.join(a)
print content

a = ['a','b','c','d']
content = ''
content = '%s%s' % tuple(a)
print content


(SELECT `zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/news.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30) union all (SELECT `zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/zg.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30) union all (SELECT `zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/gj.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30) union all (SELECT `zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/yx.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30) union all (SELECT `zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`,`zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/yl.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30) union all (SELECT`zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/cz.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30) union all (SELECT `zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/ty.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30) union all (SELECT `zb_rss_source` AS `source`, `zb_item_pubdate` AS `pubDate`,`zb_item_title` AS `title`, `zb_item_description` AS `description` FROM `zaobao_rss` WHERE `zb_rss_source` = 'http://www.zaobao.com/ssi/rss/wencui.xml' ORDER BY `zb_item_pubdate` DESC LIMIT 30)


http://tornadoapi.sinaapp.com/rss/?from=micronews