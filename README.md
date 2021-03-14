## CS Scripts

研究CobaltStrike时的一些副产品

### parse_beacon_keys.py

`.cobaltstrike.beacon_keys`中存储了CS通信时用来加密的RSA公私钥，所以如CrossC2，geacon等c2都需要解析这个文件，CrossC2怎么弄得我不知
道，但是找了找，网上基本都是用Java进行解析

这个文件本身其实就是一个KeyPair的Java对象，Python的`javaobj-py3`库可以直接读取里面存储的数据。

