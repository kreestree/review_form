# django_review_form
<h1>Введение | Introduction</h1>
<div>
  Проект создан для реализации на производстве. Представляет из себя форму для обратной связи с возможностью создания заявки с описанием проблемы и прикреплением  до 10 фото.<br>
  Обработка заявок доступна после авторизации под учетной записью с необходимыми группами разрешений.
</div>
<br>
<div>
  The project was created for implementation in production. It is a feedback form with the possibility of creating an application with a description of the problem and attaching up to 10 photos.<br>
  Application processing is available after authorization under an account with the required permission groups.
</div>

<br>

<h1>Установка | Installation</h1>
<div>
  1) Клонировать репозиторий<br>
  2) Создать .env файл с указанием переменной <code>SECRET_KEY</code><br>
  3) Применить миграции командой <code>python manage.py migrate</code><br>
  4) Создать записи в БД командой <code>python manage.py create_test_records</code>
</div>
<br>
<div>
  1) Clone the repository<br>
  2) Create a .env file specifying the <code>SECRET_KEY</code> variable<br>
  3) Apply migrations with <code>python manage.py migrate</code> command<br>
  4) Create records in the database with the command <code>python manage.py create_test_records</code><br>
</div>


