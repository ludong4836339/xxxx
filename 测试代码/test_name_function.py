import unittest   # unittest 单元测试
from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    '''测试name_function.py'''
    def test_first_last_name(self):
        '''能够正确地处理像Janis Joplin这样的姓名吗？'''
        formatted_name1=get_formatted_name('Janis','Jolin')
        self.assertEqual(formatted_name1,'Janis Jolin','断言失败')
        formatted_name2 = get_formatted_name('鲁', '冬')
        self.assertEqual(formatted_name2,'鲁 冬')
if __name__=='__main__':
    unittest.main()
