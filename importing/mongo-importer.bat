TITLE MongoDB CSV Importer
SET "MONGO_HOME=C:\Program Files\MongoDB\Server\3.6"
SET db=datasets

for %%v in (*.csv) do "%MONGO_HOME%\bin\mongoimport.exe" -d %db% -c %%~nv --type CSV --file %%v --headerline --drop
TITLE "Import completed!"
PAUSE