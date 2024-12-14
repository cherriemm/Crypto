# 



## 2 RSA Calculator

https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html



### RSA 加密/解密的过程：

1. **计算 N 和 r**：
   - 输入 `q` ,`p`
   
   - 计算 `N = p * q` , `r = (p - 1)*(q - 1)`。
   
2. **寻找模 r 同余 1 的可分解数 K**：

   - 基于的 `p` , `q` 的值，从 模`r` 同余 1 的候选数列表选择一个值 `K`，然后对K进行因式分解.

1. **寻找满足条件的 e 和 d**：
   - `K = e * d` 满足 `e*d = 1 mod r` ， 且 `e` ， `d` 分别与 `r` 互素



![image-20241020211457534](https://s2.loli.net/2024/10/20/nJFK2BGlpyquaAg.png)

![image-20241020211732236](https://s2.loli.net/2024/10/20/XWNRtLhos4mkFdA.png)







## 3 OpenSSL 实践

https://www.openssl.org

```
openssl genrsa out rsa_2048_priv.pem 2048
openssl rsa pubout in rsa_2048_priv.pem out rsa_2048_pub.pem
openssl rsautl encrypt inkey rsa_2048_pub.pem pubin in plaintext.txt out ciphertext.txt
openssl rsautl decrypt inkey rsa_2048_priv.pem in ciphertext.txt out plaintext2.txt
```







## 4 yafu 的大整数分解

https://sourceforge.net/projects/yafu/

http://www.factordb.com/
