/*This Program uses Fermat's Little Theorem*/

/*References -- 
				1) http://en.wikipedia.org/wiki/Fermat_primality_test
				2) http://en.wikipedia.org/wiki/Fermat%27s_little_theorem
				3) https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/introduction
				4) https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/
				5) https://www.khanacademy.org/computing/computer-science/cryptography/random-algorithms-probability/p/level-10-fermat-primality-test
				6) https://www.khanacademy.org/computing/computer-science/cryptography/random-algorithms-probability/v/fermat-primality-test-prime-adventure-part-10

Important Algo's used -- Fast Modular Exponentiation,Fast Modular Multiplication -- This two functions are truly important.
*/

#include <iostream>
#include <cstdlib>
using namespace std;
bool fermat(unsigned long long int c,int i);
unsigned long long int gcd(unsigned long long int x,unsigned long long int y);
unsigned long long int fastmodular(unsigned long long int l,unsigned long long int c,unsigned long long int x);
unsigned long long modmult(unsigned long long a,unsigned long long b,unsigned long long mod);
int main(void)
{
    int x;
    cin >> x;
    int j;
    for (j=0;j<x;j++)
    {
        unsigned long long int c;
        cin >> c;
        int i;
        if (c==2)
        {
            cout <<"YES\n";
            continue;
        }
        //cout <<"Enter the number of iterations.";
        //cin >> i;
        i =10;
        bool x = fermat(c,i);
        if (x)
        {
            //cout <<"It is Prime.\n";
            cout << "YES\n";
        }
        else
        {
            //cout << "It is not a prime.\n";
            cout <<"NO\n";
        }
    }
    return 0;
}

bool fermat(unsigned long long int c,int i)
{
    int k;
    for (k=0;k<i;k++)
    {
        unsigned long long int l;
        l = rand()%(c-2)+2;
        //cout << l <<"\n";
        //cout << gcd(l,c)<<"\n";
        if (gcd(l,c)!=1)
        {
            //cout << "Program Fucked up\n";
            return false;
        }
        else
        {
            //cout << "Fast Modular Working\n";
            if (fastmodular(l,(c-1),c)!=1)
            {
                return false;
            }
            else
            {
                continue;
            }
        }
    }
    return true;
}

unsigned long long int gcd(unsigned long long int x,unsigned long long int y)
{
    while(y!=0)
    {
        unsigned long long int r = x%y;
        x = y;
        y = r;
    }
    return x;
}

unsigned long long int fastmodular(unsigned long long int a,unsigned long long int b,unsigned long long int mod)
{
    unsigned long long int product,pseq;
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

unsigned long long modmult(unsigned long long a,unsigned long long b,unsigned long long mod)
{
    if (a == 0 || b < mod / a)
        return (a*b)%mod;
    unsigned long long sum;
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
