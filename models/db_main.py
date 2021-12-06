db.define_table('states',
                Field('state_name', requires=IS_NOT_EMPTY()),
                format='%(state_name)s')

db.define_table('sic',
                Field('sic_id', type='integer',
                      unique=True, requires=IS_NOT_EMPTY()),
                Field('description', requires=IS_NOT_EMPTY()),
                format='%(description)s'
                )

db.define_table('companies',
                Field('company_name', requires=IS_NOT_EMPTY()),
                Field('sic_desc', 'reference sic', requires=IS_IN_DB(
                    db, 'sic.id', '%(description)s')),
                format='%(company_name)s')

db.define_table('locations',
                Field('address', requires=IS_NOT_EMPTY()),
                Field('city', requires=IS_NOT_EMPTY()),
                Field('states', 'reference states', requires=IS_IN_DB(
                    db, 'states.id', '%(state_name)s')),
                Field('zip', requires=IS_NOT_EMPTY()),
                Field('phone', requires=IS_MATCH(
                    '[\d\-\(\) ]+')),
                )

db.define_table('companies_to_locations',
                Field('company_id', 'references companies', requires=IS_IN_DB(
                    db, 'companies.id', '%(company_name)s')),
                Field('location_id', 'references locations',
                      requires=IS_IN_DB(db, 'locations.id', '%(address)s'))
                )


db.define_table('activity_type',
                Field('description', requires=IS_NOT_EMPTY()),
                format='%(description)s'
                )


db.define_table('contact_type',
                Field('description', requires=IS_NOT_EMPTY()),
                )

db.define_table('contacts',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('home_address', requires=IS_NOT_EMPTY()),
                Field('home_city', requires=IS_NOT_EMPTY()),
                Field('states', 'reference states', requires=IS_IN_DB(
                    db, 'states.id', '%(state_name)s')),
                Field('home_zip', requires=IS_NOT_EMPTY()),
                Field('company_id', 'reference companies', requires=IS_IN_DB(
                    db, 'companies.id', '%(id)s %(company_name)s')),
                Field('title', requires=IS_NOT_EMPTY()),
                Field('office_phone'),
                Field('cell_phone'),
                Field('email', requires=IS_NOT_EMPTY()),
                Field('contact_type_id', 'reference contact_type',
                      requires=IS_IN_DB(db, 'contact_type.id', '%(description)s')),
                Field('speical_notes', requires=IS_NOT_EMPTY()),
                format='%(name)s'
                )




db.define_table('employees',
                Field('employee_name', requires=IS_NOT_EMPTY()),
                Field('employee_title', requires=IS_NOT_EMPTY()),
                Field('employee_account_number', requires=IS_IN_DB(db, 'auth_user.id', '%(id)s %(first_name)s %(last_name)s %(email)s')),
                Field('picture', 'upload', uploadfield='picture_file'),
                Field('picture_file', 'blob'),
                Field('employee_phone', requires=IS_MATCH('[\d\-\(\) ]+')),
                Field('employee_email', requires=IS_NOT_EMPTY()),
                Field('employee_address', requires=IS_NOT_EMPTY()),
                Field('employee_city', requires=IS_NOT_EMPTY()),
                Field('employee_state', 'reference states',
                      requires=IS_IN_DB(db, 'states.id', '%(state_name)s')),
                Field('employee_zip', requires=IS_NOT_EMPTY()),
                Field('employee_notes', requires=IS_NOT_EMPTY()),
                Field('employee_salary', requires=IS_NOT_EMPTY()),
                Field('employee_hire_date', 'datetime', requires= IS_DATE(format=T('%Y-%m-%d'))),
                  format="%(employee_name)s"
                )

db.define_table('activities',
                Field('contact_id', 'reference contacts',
                      requires=IS_IN_DB(db, 'contacts.id', '%(name)s')),
                Field('activity_type_id', 'reference activity_type', requires=IS_IN_DB(
                    db, 'activity_type.id', '%(description)s')),
                Field('activity_date', 'datetime', requires=IS_NOT_EMPTY()),
                Field('notes'),
                Field('account_manager', 'reference employees',
                      requires=IS_IN_DB(db, 'employees.id', '%(employee_name)s'))
                )


db.define_table('orders',
                Field('order_date', 'datetime', requires=IS_NOT_EMPTY()),
                Field('order_type'),
                Field('order_item', requires=IS_NOT_EMPTY()),
                Field('order_amount', requires=IS_NOT_EMPTY()),
                Field('order_notes', requires=IS_NOT_EMPTY()),
                Field('customer', 'reference contacts',requires=IS_IN_DB(db, 'contacts.id', '%(name)s')),
                Field('account_manager', 'reference employees', requires=IS_IN_DB(db, 'employees.id', '%(employee_name)s')),
                  format="%(order_item)s"
                )

db.define_table('lead_source',
            Field('description', requires=IS_NOT_EMPTY()),
            )

db.define_table('leads',
                Field('lead_name', requires=IS_NOT_EMPTY()),
                Field('account_manager', 'reference employees', requires=IS_IN_DB(db, 'employees.id', '%(employee_name)s')),
                Field('lead_phone', requires=IS_MATCH('[\d\-\(\) ]+')),
                Field('lead_email', requires=IS_NOT_EMPTY()),
                Field('lead_address'),
                Field('lead_city'),
                Field('lead_state', 'reference states', requires=IS_IN_DB(
                    db, 'states.id', '%(state_name)s')),
                Field('lead_zip'),
                Field('lead_notes'),
                Field('lead_source', 'reference lead_source', requires=IS_IN_DB(db, 'lead_source.id', '%(description)s')),
                )
