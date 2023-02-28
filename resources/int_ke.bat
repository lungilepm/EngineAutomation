:: Test run for int ke environment
cd C:\PycharmProjects\EngineAutomation\resources
echo [{"doc": "int_ke","env": "int"}] > envs.json
cd C:\PycharmProjects\EngineAutomation
pytest --html=reports/int/int_ke_report.html