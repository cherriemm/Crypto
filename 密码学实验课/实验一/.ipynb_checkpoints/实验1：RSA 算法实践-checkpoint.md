# 实验1：RSA 算法实践





## 1素数筛选和测试算法

在1-100000 整数中，编程实现打印所有素数，并输出素数个数，编程语言不限







## 2 RSA Calculator

实践 https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html

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
