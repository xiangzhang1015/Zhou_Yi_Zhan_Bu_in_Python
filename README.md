# Zhou_Yi_Zhan_Bu (周易占卜）

#### Authors: [Xiang Zhang](http://xiangzhang.info/) (xiang_zhang@hms.harvard.edu)

## Overview
传统的周易占卜需要五十或五十五根蓍草，且费时费力。三变为一爻，六爻为一卦，常常需要一个小时才能得出结果。本项目以Python程序模拟蓍草占卜过程，一秒钟即可得到本卦，变卦，变爻等卦象，极为简单便捷。

玩笑之谈，方家莫笑。


### Running the code

For example, to check the performance of GCN without defense under direct targeted attack, run the following code:
```
python Nettack-Di.py --dataset Cora  --modelname GCN --GNNGuard False
```

## Requirements 

GNNGuard is tested to work under Python >=3.5. 

###

第一种情况：算出来的六爻当中只有一个爻是变爻，也就是说，6个数字中有5个不是7就是8，只有1个是9或者6，这个时候，就用本卦变爻的爻辞来判断吉凶。

　　第二种情况：有两个变爻，这就是我们方才遇到的情况，这里就不再赘述了。

　　第三种情况：有三个变爻，就不能用变爻的爻辞来判断了，得用本卦和变卦的卦辞，以本卦的卦辞为主。

　　第四种情况：有四个变爻，这时就用变卦的两个不变爻的爻辞来判断吉凶。

　　第五种情况：有五个变爻，用变卦的那一个不变爻的爻辞来判断吉凶。

　　第六种情况：有六个变爻，这得分两种情况。一是六爻都是阳爻（构成了乾卦），或者六爻都是阴爻（构成了坤卦），那么，如果是乾卦，就用乾卦“用九”的爻辞判断吉凶，如果是坤卦，就用坤卦“用六”的爻辞判断吉凶。（什么是“用九”和“用六”，下文再仔细说。）二是除了这两种情况之外的其他六爻全变的情况，就用变卦的卦辞来判断吉凶。

　　第七种情况：六爻一个都没变，这时用本卦的卦辞来判断吉凶。
  
## Reference

[1] http://www.guoxue123.com/new/0001/zyjh/003.htm (占卜， 熊逸，《周易江湖》）
[2] http://www.guoxue123.com/new/0001/zyjh/004.htm (变卦， 熊逸，《周易江湖》）
[3] https://www.guoyi360.com/yj/ （解卦，卦辞，爻辞；任何周易相关的书籍网站都可以，此处以国易堂为例）
  
## Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <xiang_zhang@hms.harvard.edu>.

## License

This Zhan Bu program is licensed under the MIT License.


