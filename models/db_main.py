db.define_table('states',
                Field('state_id', requires=IS_NOT_EMPTY()),
                Field('state_name', requires=IS_NOT_EMPTY()),
                )
                
db.define_table('sic',
                 Field('sic_id', type='integer' ,unique=True, requires=IS_NOT_EMPTY()),
                 Field('description', requires=IS_NOT_EMPTY()),
                 format='%(description)s'
                 )

db.define_table('companies',
                Field('company_name', requires=IS_NOT_EMPTY()),
                Field('sic_desc', 'reference sic', requires=IS_IN_DB(db, 'sic.id', '%(description)s' ))
                )

db.define_table('locations',
                Field('address', requires=IS_NOT_EMPTY()),
                Field('city', requires=IS_NOT_EMPTY()),
                Field('states', 'reference states', requires=IS_IN_DB(db, 'states.id', '%(state_name)s')),
                Field('zip', requires=IS_NOT_EMPTY()),
                Field('phone', requires=IS_MATCH(
                    '[\d\-\(\) ]+')),
                )

db.define_table('companies_to_locations',
                Field('company_id', 'references companies', requires=IS_IN_DB(db, 'companies.id', '%(company_name)s')),
                Field('location_id', 'references locations', requires=IS_IN_DB(db, 'locations.id', '%(address)s'))
)


db.define_table('activity_type',
                Field('description', requires=IS_NOT_EMPTY()),

                )


db.define_table('contact_type',
    Field('description', requires=IS_NOT_EMPTY()),

)

db.define_table('contacts', 
    Field('name', requires=IS_NOT_EMPTY()),
    Field('home_address', requires=IS_NOT_EMPTY()),
    Field('home_city', requires=IS_NOT_EMPTY()),
    Field('states', 'reference states', requires=IS_IN_DB(db, 'states.id', '%(state_name)s')),
    Field('home_zip', requires=IS_NOT_EMPTY()),
    Field('company_id', 'reference companies' , requires=IS_IN_DB(db, 'companies.id', '%(id)s %(company_name)s')),
    Field('title', requires=IS_NOT_EMPTY()),
    Field('office_phone'),
    Field('cell_phone'),
    Field('email', requires=IS_NOT_EMPTY()),
    Field('contact_type_id', 'reference contact_type', requires=IS_IN_DB(db, 'contact_type.id', '%(description)s'))
)


db.define_table('activities',
                Field('contact_id', 'reference contacts', requires=IS_IN_DB(db, 'contacts.id', '%(name)s' )),
                Field('activity_type_id', 'reference activity_type', requires=IS_IN_DB(db, 'activity_type.id', '%(description)s')),
                Field('activity_date', 'datetime', requires=IS_NOT_EMPTY()),
                Field('notes'),
                Field('in_contact', 'reference contacts', requires=IS_IN_DB(db, 'contacts.id', '%(name)s'))
                )
   