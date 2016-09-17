/**********************Algorithms used in problem ******************************/
/***********************************
 *Pollard Rho Integer Factorization
 **Fast Modular Exponentiation
 ***Modular Multiplication
 ****Euclidean Algorithm for GCD
 *****Rabin miller Primality Test
************************************/

//Program code is given Below ---- LKID problem Medium SPOJ

#include <bits/stdc++.h>
using namespace std;
int pre[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499};
#define getcx getchar_unlocked
inline void inp( int &n )//fast input function
{
   n=0;
   int ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   n=n*sign;
}

#define pc(x) putchar_unlocked(x);
inline void wll (long long int n)
{
    register long long int N = n,rev,count = 0;
    rev = N;
    if (N == 0) { pc('0'); pc('\n'); return ;}
    while ((rev % 10) == 0) { count++; rev /= 10;} //obtain the count of the number of 0s
    rev = 0;
    while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}  //store reverse of N in rev
    while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
    while (count--) pc('0');
}

inline long long rll()
{
    int c,sign=1;
    c = fgetc(stdin);
    while ( (c < '0' || c > '9') && c != EOF )
    {
      if(c=='-')
          sign = -1;
      c = fgetc(stdin);
    }
    long long a = 0;
    while ( c >= '0' && c <= '9' )
    {
        a = (a<<3)+(a<<1) + (c - '0'); //Little probable improvement
        c = fgetc(stdin);
    }
        a = a*sign;
    return a;
}

typedef long long LL;
long long modmult(long long a,long long b,long long mod);
bool is_prime(long long int c,int i);
long long int gcd(long long int x,long long int y);
long long int fastmodular(long long int a,long long int b,long long int mod);

LL pollard_rho(LL n, LL seed) {
    LL x, y, head = 1, tail = 2;
    x = y = rand() % (n - 1) + 1;
    while (true) {
        x = modmult(x, x, n);
        x = ((x%n+seed%n)%n);
        if (x == y) {
            return n;
        }
        LL d = gcd(abs(x - y), n);
        if (1 < d && d < n) {
            return d;
        }
        head ++;
        if (head == tail) {
            y = x;
            tail <<= 1;
        }
    }
}


long long int loc = LLONG_MAX;
long long int factorize(LL n) {
    if (n > 1) {
        if (is_prime(n,7)) {
            if (n<loc)
            {
                loc = n;
            }
        } else {
            LL d = n;
            while (d >= n) {
                d = pollard_rho(n, rand() % (n - 1) + 1);
            }
            factorize(n / d);
            factorize(d);
        }
    }
    return loc;
}
/*---------------------------Fermat Primality Test is said to be slow----------------------------------*/
/*bool is_prime(long long int c,int i)
}*/
/*Miller Primality Test*/
bool is_prime(long long int p , int iterations )
{
    if(p<2)
        return false ;
    if(p!=2&&p%2==0)
        return false ;
    long long int s = p-1,a,mod,temp;
    int i;
    while(s%2==0)
        s >>= 1;
    for(i=0;i<iterations;i++)
    {
        a = rand()%(p-1)+1;
        temp = s ;
        mod = fastmodular(a,temp,p) ;
        while(temp!=p-1&&mod!=1&&mod!=p-1)
        {
            mod = modmult(mod,mod,p) ;
            temp <<= 1 ;
        }
        if(mod!= p-1&&temp%2==0)
        return false;
    }
    return true;
}

long long int gcd(long long int x,long long int y)
{
    while(y!=0)
    {
        long long int r = x%y;
        x = y;
        y = r;
    }
    return x;
}

long long int fastmodular(long long int a,long long int b,long long int mod)
{
    long long int product,pseq;
    product=1;
    pseq=a%mod;
    while(b>0)
    {
        if(b&1)
            product=modmult(product,pseq,mod);
        pseq=modmult(pseq,pseq,mod);
        b>>=1;
    }
    return product;
}

long long modmult(long long a,long long b,long long mod)
{
    if (a == 0 || b < mod / a)
        return (a*b)%mod;
    long long sum;
    sum = 0;
    while(b>0)
    {
        if(b&1)
            sum = (sum + a) % mod;
        a = (2*a) % mod;
        b>>=1;
    }
    return sum;
}

int main(void)
{
    int x;
    inp(x);
    int j,k;
    for (j=0;j<x;j++)
    {
        loc = LLONG_MAX;
        long long int y;
        y = rll();
        long long int z = y,num=0,ans;
        while(z!=0)
        {
            num=(num*10+9);
            z/=10;
        }
        ans = (num - (2*y));
        if (ans<0)
        {
            ans*=-1;
        }
        if (ans==1)
        {
            printf ("-1\n");
            continue;
        }
        int k,flag = 0;
        for (k=0;k<95;k++)
        {
            if (ans%pre[k]==0)
            {
                printf ("%d\n",pre[k]);
                flag = 1;
                break;
            }
        }
        if (flag==1)
        {
            continue;
        }
        long long int loc = factorize(ans);
        wll(loc);
        pc('\n');
    }
    return 0;
}
