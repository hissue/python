'''
for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
    *

   **

  ***

 ****

*****
'''

s=1
b=4

for i in range(5):
    print(' '*b,'*'*s)
    b-=1
    s+=1