SET dirname="%date%%time%"
set name=%dirname:/=%
set namecol=%name::=%
set name=%namecol:,=%
cd C:\PycharmProjects\EngineAutomation\resources
echo [{"doc": "int_zw","env": "int"}] > envs.json
cd C:\PycharmProjects\EngineAutomation
pytest --html=reports/int/int_zw/int_zw_%name%_report.html