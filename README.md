"# Charging-Station-Distance-Calculator" 

This is a Major project submission to the Meta Scifor Technologies Internship Program.

Project setup:
1. Created a folder with name Charging-Station-Distance-Calculator.
2. Created Virtual Environment E-V but the folder is not pushed to repo.
3. Started project with Django with command "django-admin startproject ev_distance". This creates a new folder ev_folder.
4. Made a application in project with name cal_station using command "python manage.py startapp cal_station".
5. For this project PostgreSQL databse is used for convinence of using PostGIS (Global Co-ordination Systems), necessary modifications are made in ev_distance/setting.py file. So, Django can connect to right database.
6. Before, step 3, install all dependencies like GDAL, PostGIS and PostgreSQL in system/computer.

Final Goal: Make a website to calculate and compare the distance of nearest EV Charging Station at a location.
