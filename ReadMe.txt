-1) ��������� � ��������� ����� path c:\python27;c:\python27\scripts
0) ��������� ��������� ������� � ���� �� ����������
1) ���������� python 2.7.9 (�� � ���������� TLS). ����� ���������� ������� ������ �����.
2) ���������� pyserial 2.7 �� ������������ (��� ����� pip install...)
3) �������� PIP ( python -m pip install -U pip )
4) ���������� paramiko 2.0.2 ( pip install paramiko==2.0.2 )
5) ����������� ��� ����� � c:\horizon_test\
6) ���������� ������� �/�: netsh interface ip set address "Horizon" static 10.0.0.1 255.0.0.0
7) ��������� ������� : route add 10.0.3.0 mask 255.255.255.0 10.0.0.7 -p
 