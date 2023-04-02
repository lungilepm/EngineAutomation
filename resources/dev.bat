SET dirname="%date%%time%"
set name=%dirname:/=%
set namecol=%name::=%
set name=%namecol:,=%
:: Test run for dev ke environment
cd C:\PycharmProjects\EngineAutomation\resources
echo [{"doc": "dev_ke","env": "dev"}] > envs.json
cd C:\PycharmProjects\EngineAutomation
pytest --html=reports/dev/dev/dev_%name%_report.html