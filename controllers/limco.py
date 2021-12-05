
def importp():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join("ClevelandCodesProject", 'static', "LIMCO.CSV"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            Name = line[0]
            Email = line[1]
            Office_Phone = line[2]
            Cell_Phone= line[3]
            Home_Address = line[4]
            Home_City = line[5]
            State = line[6]
            Zip_Code= line[7]
            Company = line[8]
            Title = line[9]
            contact_type=line[10]
            db.personal.update_or_insert(Name=Name, Email=Email, Office_Phone=Office_Phone, Cell_Phone=Cell_Phone, Home_Address=Home_Address,
            Home_City=Home_City, State=State, Zip_Code=Zip_Code, Company=Company, Title=Title, contact_type=contact_type)
            lines += 1
        session_lines = lines
        response_flash = str(lines) + " lines read"
    except Exception  as e:
        response_flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()
VIEW - import_results.html
{{extend 'layout.html'}}
<h1>This is the import_results.html template</h1>
<h2>
    LINES: {{=session.lines}}
</h2>
{{=BEAUTIFY(response._vars)}}