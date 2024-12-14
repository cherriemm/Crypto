#include <stdio.h>
#include <stdlib.h>

// 407开发板需要注释此句
// typedef unsigned long long ulong;

const int BASE = 2;
// 输入任意三个参数m d n，计算 m^d mod n 的值
ulong m = 13/* 补充此处参数 */;
ulong d = 5/* 补充此处参数 */;
ulong n = 17/* 补充此处参数 */;
int out;
int len, i;
uint8_t msg[5];

struct Montgomery {
    ulong m;
    ulong rrm;
    int n;
};
 
int bitLength(ulong v) {
    int result = 0;
    while (v > 0) {
        v >>= 1;
        result++;
    }
    return result;
}
 
ulong modPow(ulong b, ulong e, ulong n) {
    ulong result = 1;
 
    if (n == 1) {
        return 0;
    }
 
    b = b % n;
    while (e > 0) {
        if (e % 2 == 1) {
            result = (result * b) % n;
        }
        e >>= 1;
        b = (b * b) % n;
    }
 
    return result;
}
 
struct Montgomery makeMontgomery(ulong m) {
    struct Montgomery result;
 
    if (m == 0 || (m & 1) == 0) {
        fprintf(stderr, "m must be greater than zero and odd");
        exit(1);
    }
 
    result.m = m;
    result.n = bitLength(m);
    result.rrm = (1ULL << (result.n * 2)) % m;
 
    return result;
}
 
ulong reduce(struct Montgomery mont, ulong t) {
    ulong a = t;
    int i;
 
    for (i = 0; i < mont.n; i++) {
        if ((a & 1) == 1) {
            a += mont.m;
        }
        a = a >> 1;
    }
 
    if (a >= mont.m) {
        a -= mont.m;
    }
    return a;
}
 
int check(ulong x1, ulong x2, ulong m) {
    struct Montgomery mont = makeMontgomery(m);
    ulong t1 = x1 * mont.rrm;
    ulong t2 = x2 * mont.rrm;
 
    ulong r1 = reduce(mont, t1);
    ulong r2 = reduce(mont, t2);
    ulong r = 1ULL << mont.n;
 
    ulong prod = reduce(mont, mont.rrm);
    ulong base = reduce(mont, x1 * mont.rrm);
    ulong exp = x2;
    // 进行模幂运算前将引脚8电压拉高
    digitalWrite(8, HIGH);
    while (bitLength(exp) > 0) {
     // 每次循环开始将引脚7电压拉高，结束将引脚7电压拉低
    digitalWrite(7, HIGH);
        if (exp % 2 == 1) {
            prod = reduce(mont, prod * base);
        }
        exp >>= 1;
          base = reduce(mont, base * base);
    digitalWrite(7, LOW);
    }
    // 模幂运算结束后将引脚8电压拉低
    digitalWrite(8, LOW);
    out = reduce(mont, prod);
    return out;
}
//开发板初始化  
void setup() {
  Serial.begin(115200);//串口初始化 PD0-RXD PD1-TXD
  pinMode(8, OUTPUT);//Trigger 引脚初始化 8
  pinMode(7, OUTPUT);//Trigger 引脚初始化 8
  Serial.println("RESTART");
} 
void loop() {
  //如果输入缓冲区长度等于5，就将数据读到msg中
  if(Serial.available()== 5){
    Serial.readBytes(msg, 5);
    // 计算m的d次幂模n的结果
    out = check(m,d,n);
    // 串口输出结果
    Serial.println(out);
    // 串口打印FINISH
    Serial.println("FINISH");
    }

}
