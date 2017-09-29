def digit_by_digit_square_root(n):
    arr = 1
    i = 1
    while(i*i <= n):
        i  = i + 1
    q1 = i - 1
    q2 = q1
    n = (n - (q1*q2))*100

    if(n == 0):
        ans = 0
    else:
        ans = q1
        while(n != 0 and arr != 100):
            q2 = 20*q1
            cnt = 0
            while((q2 + cnt)*cnt < n):
                cnt = cnt + 1
            cnt = cnt - 1
            ans = ans + cnt
            arr = arr + 1
            q1 = (q1*10) + cnt
            n = (n - (q2 + cnt)*cnt) * 100 

    return ans       

sq = 0
for i in range(2, 100):
    sq = sq + digit_by_digit_square_root(i)

print(sq)
        
   
        
        
     
    
