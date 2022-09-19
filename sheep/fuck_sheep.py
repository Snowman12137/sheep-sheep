"""

简化版羊了个羊脚本
原作者：lcry
@author : xiaofeifei
@time : 2022/9/19
"""
import random
import requests
import urllib3
import time
import sys





#↓↓↓↓↓↓↓↓↓↓↓↓
token = "" #需要抓包拿token，UUID可以转换合法token，但是很麻烦
#↑↑↑↑↑↑↑↑↑↑↑填这里然后再运行
count = 2 #通关次数

finish_api = "https://cat-match.easygame2021.com/sheep/v1/game/game_over_ex" #2022/9/19
#完成羊群接口


request_header = {
    "Host": "cat-match.easygame2021.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN",
    "t": token,
    "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/17/page-frame.html",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "Connection": "close"
}


def wait_for_random_interval(is_show):
    interval_time = random.randint(2, 6)
    if is_show:
        print(f"等待随机时间间隔，防止游戏服务器接口限流导致失败 : {interval_time} s")
    time.sleep(interval_time)


def finish_game_sheep(skin, rank_time): 
    s = requests.session() 
    s.keep_alive = False 
    finish_body = {"rank_score": 1, "rank_state": 1, "rank_time": rank_time, "rank_role": 1, "skin": 1, "MatchPlayInfo": "CAMiBQjnARAAIgYI5gEQ2wEiBgiAAhDWASIGCP8BEN8BIgYInwIQsAQiBgieAhCQAyIGCJwCENEH"} 
    res = requests.post(finish_api, data=finish_body, headers=request_header, timeout=10, verify=True) # err_code为0则成功 
    if res.json()["err_code"] == 0: 
        print("[恭喜你! 本次闯关羊群状态成功]") 
    else: 
        print(res.json()) 
        print("请检查t的值是否获取正确!")



if __name__ == '__main__':
    if token = "":
        print("请先填写token")
        exit(0)
    if count > 10 :
        print("不要这么多啦")
        print("闯关over")
        sys.exit(0)
    success = 0
    i = 1
    while True:
        print(f"...第{i}次尝试完成闯关...")
        cost_time = random.randint(1, 3600)
        print(f"生成随机闯关完成耗时: {cost_time} s")
        try:
            wait_for_random_interval(True)
            finish_game_sheep(1, cost_time)
            success += 1
        except Exception as e:
            print(f"游戏服务器响应超时或崩溃中未及时响应，缓缓吧，等待服务器恢复后再试！本次失败请忽略，错误日志: {e}")
            sys.exit(0)
        if success >= count:
            print("【羊了个羊一键闯关结束】")
            sys.exit(0)
        print(f"\033[4;32m已成功完成{success}次\033[0m")
        i += 1



