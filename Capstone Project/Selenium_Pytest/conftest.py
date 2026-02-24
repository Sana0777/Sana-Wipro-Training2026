import pytest
import shutil
import os
from datetime import datetime
from utilities.browser import get_driver, get_base_url

os.makedirs("reports",     exist_ok=True)
os.makedirs("screenshots", exist_ok=True)


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",  None)
    metadata.pop("Plugins",    None)
    metadata.pop("JAVA_HOME",  None)


def pytest_html_report_title(report):
    report.title = "UI Automation PYTEST Report"


@pytest.fixture(scope="function")
def driver():
    web_driver = get_driver()
    web_driver.get(get_base_url())
    yield web_driver
    web_driver.quit()

_current_step: dict[str, str] = {}

def set_step(step_name: str, request):

    _current_step[request.node.nodeid] = step_name

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report  = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            ts   = datetime.now().strftime("%Y%m%d_%H%M%S")

            step = _current_step.get(item.nodeid, "")
            if step:
                filename = f"FAIL_{step}_{ts}.png"
            else:
                test_name = item.originalname if hasattr(item, "originalname") \
                            else item.name.split("[")[0]
                filename = f"FAIL_{test_name}_{ts}.png"

            path = os.path.join("screenshots", filename)
            drv.save_screenshot(path)


        _current_step.pop(item.nodeid, None)

def pytest_sessionfinish(session, exitstatus):
    ts          = datetime.now().strftime("%d%b%Y_%H%M").upper()
    src         = os.path.join("reports", "report.html")
    dst         = os.path.join("reports", f"report_{ts}.html")
    if os.path.exists(src):
        shutil.copy(src, dst)
        os.remove(src)