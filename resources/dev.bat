:: Test run for dev ke environment
cd C:\PycharmProjects\EngineAutomation\resources
echo [{"doc": "dev_ke","env": "dev"}] > envs.json
cd C:\PycharmProjects\EngineAutomation
pytest --html=reports/dev/dev_ke_report.html