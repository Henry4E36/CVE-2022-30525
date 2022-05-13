import random
import requests

res = requests.session()


def get_dnslog():
    t = random.random()
    url = f"http://www.dnslog.cn/getdomain.php?t={t}"
    res1 = res.get(url=url)
    if res1.status_code == 200 and "dnslog" in res1.text:
        dnslog = res1.text
        return dnslog
    else:
        print("获取dnslog失败")


def get_data():
    t = random.random()
    url = f"http://www.dnslog.cn/getrecords.php?t={t}"
    res2 = res.get(url=url)
    return res2.text



