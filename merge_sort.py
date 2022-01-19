data_list = [1,9,3,2,8]

def split_func(data_list):
    medium = int(len(data_list) / 2)
    print (data_list[:medium])
    print (data_list[medium:])

split_func(data_list)