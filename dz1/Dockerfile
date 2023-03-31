# образ Python
FROM python:3.10   
# переменная среды DockerHOME
ENV DockerHOME=/home/app/micsrvc_dz1
# создание рабочего каталога  
RUN mkdir -p $DockerHOME  
# задание рабочего каталога  
WORKDIR $DockerHOME  
# переменная среды для перенаправления стандартного вывода Python в консоль Docker
ENV PYTHONUNBUFFERED 1  
# Установка зависимостей
RUN pip install --upgrade pip  
# копирование проекта в рабочегую директорию
COPY . $DockerHOME  
# установка зависимостей  
RUN pip install -r requirements.txt
# порт для приложения Django  
EXPOSE 8000  
# запуск Django приложения  
CMD python main.py