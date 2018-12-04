from gevent import monkey

monkey.patch_socket()
import gevent

quere = []


def f(n):
    print(n['url'], type(n['url']))
    for i in n['url']:
        print(gevent.getcurrent(), n['header'], i)
        item = {}
        item['heard'] = n["header"]
        item['url'] = n['url']
        item['test'] = 'test'
        print(item)
        quere.append(item)


header = {
    "test": "ajgigj"
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "accept-language": "ZH-cn,zh;q=0.9",
    # "cache-control": "max-age=0",
    # "connection": "keep-alive",
    # "host": "bj.lianjia.com",
    # "referer": "https://bj.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo&ljref=pc_sem_baidu_ppzq_x",
    # "upgrade-insecure-requests": "1",
    # "user-agent": "mozilla/5.0 (windoWS NT 10.0; Win64; x64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/69.0.3497.100 safari/537.36"
}
g1 = gevent.spawn(f, {'header': header, 'url': [3, 6, 8, 3, 2]})


# g2 = gevent.spawn(f, [3, 6, 8, 3, 2])
# g3 = gevent.spawn(f, [2, 2, 2, 2, 22, 2])
# g1.join()
# g2.join()
# g3.join()
# print(g1, type(g1))
# for i in g1:
#     print(i)
#
# from gevent import monkey; monkey.patch_all()
# import requests
# # import
#
# def f(url):
#     print('GET: %s' % url)
#     resp = requests.get(url)
#     data = resp.text
#     print('%d bytes received from %s.' % (len(data), url))
# #
# # # gevent.joinall([
# # #         gevent.spawn(f, ['https://www.python.org/', 'https://github.com/']),
# # #         gevent.spawn(f, 'https://www.yahoo.com/'),
# # #         # gevent.spawn(f, ),
# # # ])
# #
# # # gevent.joinall([
# # #                 # gevent.spawn_raw(f, ['https://www.python.org/', 'https://github.com/']),
# # #                 gevent.spawn(f, 'https://www.yahoo.com/'),
# # # ])
# urls = ['https://www.python.org/', 'https://github.com/']
# #
# gevent.joinall([gevent.spawn(f, x) for x in urls])

def not_empty(s):
    print(s)
    return s%2==0


# a = filter(not_empty, ['A', '', 'B', None, 'C', '  '])
a = filter(not_empty, [5,6,3,8,6,9])
print(list(a))