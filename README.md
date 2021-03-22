## CS Scripts

研究CobaltStrike时的一些副产品

### parse_beacon_keys.py

`.cobaltstrike.beacon_keys`中存储了CS通信时用来加密的RSA公私钥，所以如CrossC2，
geacon等c2都需要解析这个文件，CrossC2怎么弄得我不知道，但是找了找，网上基本都是用
Java进行解析

这个文件本身其实就是一个KeyPair的Java对象，Python的`javaobj-py3`库可以直接读取里面存储的数据。

主要好处是无视serialVersionUID导致的版本兼容性问题，同时Python的启动速度较Java较快

### csbruter

来源：https://github.com/ryanohoro/csbruter

暴力破解Cobalt Strike团队服务器密码的脚本。

忧郁Cobalt Strike 3.10（于2017年12月11日发布）在尝试之间施加了1秒的延迟，以缓解
此攻击，目前爆破的效果不是很好。

此处仅做收集，后续有需要可以考虑用Golang重构或者优化爆破脚本