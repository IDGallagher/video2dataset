import s3fs
s3 = s3fs.S3FileSystem(anon=False)
s3.ls('webvid10m-test')
with s3.open('webvid10m-test/test.csv', 'rb') as f:
    print(f.read())