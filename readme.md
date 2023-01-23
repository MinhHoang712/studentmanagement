
**Giới Thiệu:** 
<space><space>
Studentmanagement là một trang web với nội dung quản lý sinh viên dành cho trường học, với các tính năng cơ bản như quản lý sinh viên, nhân viên nhà trường, quản lý môn học, học kỳ, và các tính năng đang được phát triển.

##Công cụ phát triển 
- Python 3.10.8
- Django 4.0.1
- SQLITE3 3.37.2
##Cách cài đặt

1. Cài đặt python từ trang chủ https://www.python.org/ 
2. Tạo thư mục mới, tải xuống toàn bộ project studentmangement và lưu vào đó
3. Mở Terminal và dẫn đường dẫn tới thư mục vừa tạo, gõ python -m pip install --user virtualenv để tải package môi trường ảo 
4. Sau khi tải, nhập python -m venv venv để tạo thư mục môi trường ảo 
5. venv\Scripts\activate để khởi động môi trường ảo, rồi mở thư mục project trong Terminal
6. Nhập liên tiếp hai lệnh: python manage.py makemigrations và python manage.py migrate
7. python manage.py createsuperuser để tạo tài khoản admin hệ thống
8. python manage.py runserver để khởi tạo project trên nền web, đăng nhập bằng tài khoản admin 
   
