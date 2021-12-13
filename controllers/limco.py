def importp():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "contacts.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            id = line[0]
            first_name = line[1]
            last_name = line[2]
            email = line[3]
            office_phone = line[4]
            cell_phone =line[5]
            home_address = line[6]
            home_city = line[7]
            states = line[8]
            home_zip = line[9]
            company = line[10]
            title = line[11]
            contact_type_id=line[12]
            industry=line[13]
            company_id = db.companies.update_or_insert(company_name=company,sic_desc=industry)
            states = db.states.update_or_insert(state_name=states)
            db.contacts.update_or_insert(company_id=company_id, states=states,
            description=industry, first_name=first_name, last_name=last_name, email=email, 
            office_phone=office_phone, cell_phone=cell_phone,
            home_address=home_address, home_city=home_city, 
            home_zip=home_zip, company_name=company, title=title,contact_type_id=contact_type_id,
            )  
          
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
        session.msg=str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = ("import_results.html")
    return dict()

