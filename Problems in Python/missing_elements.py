# missing element in 2nd Array

arr_one=list(map(int,input("First list: ").split(',')))
arr_two=list(map(int,input("Second list: ").split()))

def missing(a_one,a_two):
    mis_array=[]
    for e in a_one:
        if e not in a_two:
            mis_array.append(e)
        else:
            continue
    print(f"Missed elements are {mis_array} ")

missing(arr_one,arr_two)
"""
LEETCODE PROBLEM 231


class Solution {
    public boolean isPowerOfTwo(int n) {
        int m =3;
        if (n==1){
            return true;
        }
        while (m <=n){
            if (n%2==0){
                if (n>=3){
                    n=n/2;
                }
            }else{
                n=1;
            }
        }
        if (n==2){
            return true;
        }else{
            return false;
        } 
    }    
}


"""
