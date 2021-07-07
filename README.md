# polls_full_stack_drf_and_react

Eng

###Installation

open terminal

pip install pipenv

mkdir polls

cd polls

clone https://github.com/EHGWRabbit/polls_full_stack_drf_and_react.git

cd polls_full_stack_drf_and_react

pipenv shell

pipenv install django==2.2.10

pipenv install coreapi==2.3.3

pipenv install pyyaml==5.1

pipenv install django-rest-swagger==2.2.0

pipenv install djangorestframework

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

open browser

go to localhost:8000 (alt:127.0.0.1:8000)




FRONTEND

cd frontend


npx create-react-app 

yarn start

localhost:3000
P.S. change in root settings WHITELIST = 3001 on 3000 for react network with api



РУССКИЙ

###УСТАНОВКА

откройте терминал

установите

pip install pipenv

создайте папку

mkdir polls

перейдите в нее

cd polls

скачайте репозиторий

clone https://github.com/EHGWRabbit/polls_full_stack_drf_and_react.git


перейдите в корневую папку репозитория
cd polls_full_stack_drf_and_react

запустите оболочку 


pipenv shell

вы можете воспользоваться командой pipenv install -r requirements.txt

а можете этого не делать, дабы удостовериться лишний раз в правильности установки

pipenv install django==2.2.10

pipenv install coreapi==2.3.3

pipenv install pyyaml==5.1

pipenv install django-rest-swagger==2.2.0

pipenv install djangorestframework(любую)


совершаем синхронизацию в два шага 

python manage.py makemigrations  первый

python manage.py migrate  второй

запускаем сервер разработки
python manage.py runserver

открываем браузер
open browser

кому лень набирать в строке браузера - скопируйте или отсюда или из командной строки
go to localhost:8000 (alt:127.0.0.1:8000)




FRONTEND

перейти в папку 
cd frontend

запустить
npx create-react-app 

запустить
yarn start

перейти
localhost:3000
P.S. change in root settings WHITELIST = 3001 on 3000 for react network with api

у автора был занят порт 3000 так что пришлось использовать 3001
в настройках проекта по умолчанию стоит 3001 так что имейте это ввиду, запуская приложение.


Еще имейте ввиду, что тесты не прописаны, а следовательно, не факт, что приложение будет работать именно так, как задумал я) улыбнитесь, если что)



