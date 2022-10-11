x = '300 Bemidji Ave N, Bemidji, MN 56601'
    
my_list = [56601,56633,56630,56676,56725,56727,56678,56670,56667,56666,56663,56647,56650,56683,56685,56671,56687,56619]

if len(x) > 5:

    if x.count(' ') > 1:

        if x.count(',') > 0:

            c = x.split(' ')[-1]

            if int(c) in my_list:

                print('Yes')
            
else:
    print('No')