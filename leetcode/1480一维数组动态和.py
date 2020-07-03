def runingSum(ls):
    sum_list = []
    for i, n in enumerate(ls):
        new_ls = ls[0:i+1]
        sum_list.append(sum(new_ls))
    print(sum_list)

ls = [1,2,3,4]
runingSum(ls)
