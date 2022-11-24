
Для запуска автотестов необходимо:
1) Установить зависимости: pip install -r requirements.txt
2) В терминале ввести команду python -m pytest ./path/to/test/cases.py --alluredir ./path/to/results:
   например: python -m pytest /home/user/example/tests/test_cases/cases.py --alluredir ./results -v,
    python -m pytest /home/bobur/pythonProject/TEST_TASK_HAMKORLAB/test_reqres/tests/test_cases/reqres_test_cases.py --alluredir ./test_reqres/results -v
   python -m pytest /home/bobur/pythonProject/TEST_TASK_HAMKORLAB/selenium_hamkorbank/tests/test_cases/sidebar_cases.py --alluredir ./selenium_hamkorbank/results -v



