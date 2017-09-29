a = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety','100':'hundred','1000':'onethousand','0':''}
b = []

for i in range(1, 1001):

    if i > 0 and i < 21:
        k = str(i)
        b.append(len(a[k]))

    if i > 20 and i < 100:
        m = i % 10
        i = i - m
        k1 = str(i)
        k2 = str(m)
        b.append(len(a[k1] + a[k2]))

    if i >= 100 and i < 1000:

        m1 = i // 100
        n1 = i % 100

        if n1 == 0:
            k8 = str(m1)
            b.append(len(a[k8] + a['100']))

        if n1 > 0 and n1 < 21:
            k3 = str(m1)
            k4 = str(n1)
            b.append(len(a[k3] + a['100']+ 'and' + a[k4]))

        if n1 > 20 and n1 < 100:
            k5 = str(m1)
            n2 = n1 % 10
            n1 = n1 - n2
            k6 = str(n1)
            k7 = str(n2)
            b.append(len(a[k5] + a['100'] + 'and' + a[k6] + a[k7]))
    if i == 1000:
        b.append(len(a['1000']))

print(sum(b))

            
        
        
        
        
        
