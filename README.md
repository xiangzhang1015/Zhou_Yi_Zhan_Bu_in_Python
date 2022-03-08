# 周易占卜 in Python

<font color=#ffffff>2022年于月光之下，云海之上。</font>

#### Authors: [Xiang Zhang](http://xiangzhang.info/) (xiang.alan.zhang@gmail.com)

## 概述
传统的周易占卜需要五十或五十五根蓍草，且费时费力。三变为一爻，六爻为一卦，常常需要一个小时才能得出结果。本项目以Python程序模拟蓍草占卜过程，一秒钟即可得到本卦、变卦、变爻等卦象，极为简单便捷。更为重要的是，各个卦象出现的概率与用蓍草占卜的概率相同。总之，周易占卜的Python实现极大的提高的占卜的效率却不影响结论的准确程度，实在是居家旅行的必备神器。

玩笑之谈，方家莫笑。

## 算卦
- 大衍之数五十，少一而生无穷变化。

- 开天地，定三才，除四象，归混沌，如是为一变。

- 三变为成一爻，六爻为一卦。是为本卦。

## 变卦

- 爻分阴阳，可细分为老阴、少阳、少阴、老阳。

- 老阴生少阳，老阳生少阴。阴阳互变之爻为变爻。

- 爻变而卦变，是为变卦。 

## 解卦

解卦时需要同时考虑本卦和变卦。共有七种情形：
1. 算出来的六爻当中只有一个爻是变爻，也就是说，6个数字中有5个不是7就是8，只有1个是9或者6，这个时候，就用本卦变爻的爻辞来判断吉凶。

2. 有两个变爻，这就是我们方才遇到的情况，这里就不再赘述了。

3. 有三个变爻，就不能用变爻的爻辞来判断了，得用本卦和变卦的卦辞，以本卦的卦辞为主。

4. 有四个变爻，这时就用变卦的两个不变爻的爻辞来判断吉凶。

5. 有五个变爻，用变卦的那一个不变爻的爻辞来判断吉凶。

6. 有六个变爻，这得分两种情况。一是六爻都是阳爻（构成了乾卦），或者六爻都是阴爻（构成了坤卦），那么，如果是乾卦，就用乾卦“用九”的爻辞判断吉凶，如果是坤卦，就用坤卦“用六”的爻辞判断吉凶。（什么是“用九”和“用六”，下文再仔细说。）二是除了这两种情况之外的其他六爻全变的情况，就用变卦的卦辞来判断吉凶。

7. 六爻一个都没变，这时用本卦的卦辞来判断吉凶。


*算卦和变卦的内容是我根据文献[1]故弄玄虚（无误）总结的。解卦的内容是从文献[2]粘贴来的。*

*各卦的卦辞和爻辞可从任意版本的周易的《易经》（不是《易传》）中得到。例同参考文献[3]。*

### Running the code

代码运行极为简单便捷。Clone and run the following code:
```
python Zhan_Bu.py
```

## Requirements 

The code is tested to work on plateform with Python >=3.5. 
  
## Reference

[1] http://www.guoxue123.com/new/0001/zyjh/003.htm (占卜， 熊逸，《周易江湖》）

[2] http://www.guoxue123.com/new/0001/zyjh/004.htm (变卦， 熊逸，《周易江湖》）

[3] https://www.guoyi360.com/yj/ （解卦，卦辞，爻辞；任何周易相关的书籍网站都可以，此处以国易堂为例）
  
## Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <xiang_zhang@hms.harvard.edu>.

## License

This Zhan Bu program is licensed under the MIT License.


