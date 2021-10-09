"""
文件上传助手类
"""
import uuid


class File_Upload_Helper(object):
    IMAGE_PATTERN='jpg,jpeg,gif,png,bmp'

    @classmethod
    def get_file_extname(cls, filename):
        return filename[filename.rfind('.')+1:]

    @classmethod
    def is_Image_File(cls,filename):
        ename=cls.get_file_extname(filename)
        ename=ename.lower()
        return ename in cls.IMAGE_PATTERN

    @classmethod
    def create_image_file(cls, filename):
        fname=str(uuid.uuid1()).replace('-','')[:10]
        extname=cls.get_file_extname(filename)
        return f'{fname}.{extname}'

if __name__=='__main__':
    fname='abc.JPG'
    print(File_Upload_Helper.is_Image_File(fname))
    print(File_Upload_Helper.get_file_extname(fname))
    print(File_Upload_Helper.create_image_file(fname))