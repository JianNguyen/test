import os

path = r"C:\Users\84386\Desktop\GIT\Deep-Learning-Approach-for-Surface-Defect-Detection\KolektorSDD"


def listData(data_dir):
    data_list = os.listdir(data_dir)
    # for (root, dirs, files) in os.walk(data_dir, topdown=True):
    #     # print(root)
    #     # print(dirs)
    #     print(files[0, 1])
    #     # print('--------------------------------')
    example_dirs = [x[1] for x in os.walk(data_dir)][0]
    example_lists = {os.path.basename(x[0]): x[2] for x in os.walk(data_dir)}
    print(example_dirs, example_lists )


listData(path)
