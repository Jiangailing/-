import pytest
import time
import os

now = time.strftime("%Y-%m-%d", time.localtime())
now_str = str(now)

if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    os.system("allure generate reports/ -o reports/"+now_str+"/html --clean")
