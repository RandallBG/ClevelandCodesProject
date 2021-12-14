def importp():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "employees.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            id = line[0]
            first_name = line[1]
            last_name = line[2]
            employee_title = line[3]
            employee_account_number = line[4]
            picture =line[5]
            picture_file = line[6]
            employee_phone = line[7]
            employee_email = line[8]
            employee_address= line[9]
            employee_city=[10]
            employee_state = line[11]
            employee_zip=line[12]
            employee_notes=line[13]
            employee_salary=line[14]
            employee_hire_date=line[15]
            db.contacts.update_or_insert(first_name=first_name, 
            last_name=last_name, employee_title=employee_title, employee_account_number=employee_account_number,
            picture=picture, picture_file=picture_file, employee_phone=employee_phone, employee_email=employee_email,
            employee_address=employee_address, employee_city=employee_city, employee_state=employee_state,
            employee_zip=employee_zip, employee_notes=employee_notes, employee_salary=employee_salary, 
            employee_hire_date=employee_hire_date) 

            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
        session.msg=str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = ("import_results.html")
    return dict()

