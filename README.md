# 食用说明

使用本API请具有一定基础

本程序基于 [BlackSheep](https://github.com/Neoteroi/BlackSheep) 搭建

开发环境为 `Python 3.10`

因为用到 `orjson` 所以需要安装 `rust` 以完成 `orjson` 的安装

因为基于 `BlackSheep` 所以需要 `Cython` 所以需要 `gcc`

(环境方面不再描述 环境问题按照提示处理)

本程序需要 GeoIP 库(本库不提供下载)

请自行到 [Maxmind](https://www.maxmind.com/en/accounts/216453/geoip/downloads) 下载 `GeoLite2-City.mmdb` 并放到 `src` 目录中

本程序需要 ip2asn 库(本库不提供下载)

请自行到 [iptoasn](https://iptoasn.com/) 下载 `ip2asn-v4-u32.tsv`和`ip2asn-v6.tsv` 并放到 `src` 目录中

请修改 `config.yaml.example` 更名为 `config.yaml` 可修改内的参数.

IP接口备选方案使用 [高德开放平台](https://console.amap.com/dev/key/app) 请 创建一个 Key 再将这个KEY放到 config.yaml 中的 ip->key 值

随机图库放在 `./src/img_url_mb.txt` 和 `./src/img_url_pc.txt` 中 可以自行修改其中的链接 

这里我是用的是[fghrsh](https://img.fghrsh.net) 大佬的图床 所以有处理规则

可以自行修改 `./app/routers.py` 中的 `async def Randimg`

一言库使用 [sentences-bundle](https://github.com/hitokoto-osc/sentences-bundle)

# 建议
虽然可以直接使用 `uvicorn`，但是还是建议使用 [nginx-unit](https://unit.nginx.org/installation/)

因为`nginx-unit`的性能高 如使用`nginx-unit`的话可以使用 `unit.config` 作为配置文件

需要修改`path`和`working_directory`

个人使用 unit 编译:
```
git clone https://github.com/nginx/unit
cd unit
./configure --prefix=/usr/local/unit --group=unit --user=unit --openssl --no-ipv6 --control=unix:/var/run/control.unit.sock
make && make install
```

编译 unit-python3.10:
```
./configure python --module=py310 --config=python3.10-config
make && make install
```

# 已实现功能
+ QQ昵称/头像获取
+ 一言
+ IP定位
+ UA
+ 随机图


# 待做
- [x] 为client做限制防止并发时带来的崩溃
+ bilibili_API
+ 重写ip2asn
- [x] yaml 替代 parse_it

# 更新日志

+ 2022-03-22 重写随机图模块
+ 2021-10-28 完善Config
+ 2021-10-24 修正QQAPI接口编码问题
> 做了一个有趣的实验, 将`sqlite3`替换为 `aiosqlite`.
可是替换完成之后发现一个问题.
 那就是`aiosqlite`的性能反而没有`sqlite3`的性能高.
 原因不明 所以做了回滚. 目前还是使用`sqlite3`

+ 2021-11-03 完善docs
+ 2021-10-22 避免多余的开销
+ 2021-10-21 完善docs
+ 2021-10-20 完成程序的重构 放弃 FastApi ,拥抱 BlackSheep
