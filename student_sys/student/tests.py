from django.test import TestCase, Client
from .models import Student

# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):  #必填
        Student.objects.create(
            name='wate',
            sex=1,
            email='43779120@sina.com.cn',
            profession='医生',
            qq='133267518',
            phone='15998771323',
        )


    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='lee',
            sex=2,    #整形字段赋值，万不能加引号,要不和models里的intergerField不匹配
            email='155367822@qq.com',
            profession='boss',
            qq='2289619653',
            phone='13123145959',
        )
        self.assertEqual(student.sex_show, '女', '性别字段内容和展示不一样!')

    def test_filter(self):
        Student.objects.create(
            name='siyu',
            sex=2,
            email='56738920@sina.com.cn',
            profession='列车员',
            qq='665398218',
            phone='15979877023',
        )
        name = 'lee'
        students = Student.objects.filter(name='siyu')   #名字要和你当前def创造的一样
        self.assertEqual(students.count(), 1, '应该只存在一个名字为{}的记录'.format(name))


    def test_get_index(self):
        #测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200 !')

    def test_post_student(self):
        client = Client()    #最开始忘了加括号，出现client的类型不对
        data = dict(
            name = 'test_for_post',
            sex=1,
            email='333@dd.com',
            profession='农民',
            qq='67837462',
            phone='28917737',
        )

        response = client.post('/' ,data)
        self.assertEqual(response.status_code, 302, 'status code must be 302 !')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain `test_for_post`')