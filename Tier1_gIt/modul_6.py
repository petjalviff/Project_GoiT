import shutil

for a, b, in shutil.get_archive_formats():
    print("_"*40)
    print("{:^
          10} | {:^25} |".format(a,b))
