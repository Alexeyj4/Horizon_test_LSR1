-1) Прописать в перемнную среды path c:\python27;c:\python27\scripts
0) Проверить установку времени и даты на компьютере
1) Установить python 2.7.9 (он с поддержкой TLS). Перед установкой удалить старый питон.
2) Установить pyserial 2.7 из дистрибутива (или через pip install...)
3) Обновить PIP ( python -m pip install -U pip )
4) Установить paramiko 2.0.2 ( pip install paramiko==2.0.2 )
5) Скопировать эту папку в c:\horizon_test\
6) Установить сетевой и/ф: netsh interface ip set address "Horizon" static 10.0.0.1 255.0.0.0
7) прописать маршрут : route add 10.0.3.0 mask 255.255.255.0 10.0.0.7 -p
 