def importp():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "limco.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            customer_id = line[0]
            name = line[1]
            contact_name = line[2]
            home_address= line[3]
            home_city= line[4]
            postal_code = line[5]
            country = line[6]
            company_id=db.companies.update_or_insert(company_name=name)
            db.contacts.update_or_insert(company_id=company_id, name=name, home_address=home_address, home_city=home_city,home_zip=postal_code)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
        session.msg=str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = ("import_results.html")
    return dict()

