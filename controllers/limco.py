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
            name = line[1]
            home_address = line[2]
            home_city= line[3]
            states= line[4]
            home_zip=line[5]
            company = line[6]
            title = line[7]
            office_phone = line[8]
            cell_phone = line[9]
            email=line[10]
            contact_type=line[11]
            company_id=db.companies.update_or_insert(company_name=name)
            db.contacts.update_or_insert(company_id=company_id, name=name, home_address=home_address, home_city=home_city,states=states,home_zip=postal_code)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
        session.msg=str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = ("import_results.html")
    return dict()

