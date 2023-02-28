:: Test run for int zw environment
cd C:\PycharmProjects\EngineAutomation\resources
echo [{"doc": "int_zw","env": "int"}] > envs.json
cd C:\PycharmProjects\EngineAutomation
pytest --html=reports/int/int_zw_report.html