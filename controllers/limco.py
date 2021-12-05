
def importp():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "LIMCO.CSV"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            Name = line[0]
            Email = line[1]
            Office Phone = line[2]
            Cell Phone= line[3]
            Home Address = line[4]
            Home City = line[5]
            State = line[6]
            Zip Code= line[7]
            Company = line[8]
            Title = line[9]
            contact Type=line[10]
            db.personal.update_or_insert(nick_name=nick_name, address=address, married=married, zip_code=zip_code, reg_id=reg_id)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
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