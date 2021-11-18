db.define_table('states',
                Field('state_id', requires=IS_NOT_EMPTY()),
                Field('state_name', requires=IS_NOT_EMPTY()),
                
                )
                
db.define_table('sic',
                 Field('sic_id', requires=IS_NOT_EMPTY()),
                 Field('description', requires=IS_NOT_EMPTY()),
                 )

db.define_table('companies',
                # Field('company_id', requires=IS_NOT_EMPTY()),
                Field('company_name', requires=IS_NOT_EMPTY()),
                Field('sic_id', 'reference sic', requires=IS_NOT_EMPTY()),
                redefine=True
                )

db.define_table('locations',
                Field('location_id', requires=IS_NOT_EMPTY()),
                Field('company_id', 'reference companies', requires=IS_NOT_EMPTY()),
                Field('address', requires=IS_NOT_EMPTY()),
                Field('city', requires=IS_NOT_EMPTY()),
                Field('states', requires=IS_NOT_EMPTY()),
                Field('zip', requires=IS_NOT_EMPTY()),
                Field('phone', requires=IS_MATCH(
                    '[\d\-\(\) ]+')),

                )



db.define_table('activity_type',
                Field('activity_type_id', requires=IS_NOT_EMPTY()),
                Field('description', requires=IS_NOT_EMPTY()),

                )



db.define_table('lead_source',
    Field('lead_source_id', requires=IS_NOT_EMPTY()),
    Field('description', requires=IS_NOT_EMPTY()),

)

db.define_table('contact_type',
    Field('contact_type_id', requires=IS_NOT_EMPTY()),
    Field('description', requires=IS_NOT_EMPTY()),

)

db.define_table('contacts', 
    Field('name', requires=IS_NOT_EMPTY()),
    Field('home_address', requires=IS_NOT_EMPTY()),
    Field('home_city', requires=IS_NOT_EMPTY()),
    Field('state_id', 'reference states', requires=IS_NOT_EMPTY()),
    Field('home_zip', requires=IS_NOT_EMPTY()),
    Field('company_id', 'reference companies' , requires=IS_NOT_EMPTY()),
    Field('title', requires=IS_NOT_EMPTY()),
    Field('office_phone'),
    Field('cell_phone'),
    Field('location_id', 'reference locations' ,requires=IS_NOT_EMPTY()),
    Field('email', requires=IS_NOT_EMPTY()),
    Field('contact_type_id', 'reference contact_type', requires=IS_NOT_EMPTY()),
    format='%(state_name)s'
)


db.define_table('activities',
                Field('activity_id', requires=IS_NOT_EMPTY()),
                Field('contact_id', 'reference contacts', requires=IS_NOT_EMPTY()),
                Field('activity_type_id', 'reference activity_type', requires=IS_NOT_EMPTY()),
                Field('activity_date', 'datetime', requires=IS_NOT_EMPTY()),
                Field('times', requires=IS_NOT_EMPTY()),
                Field('notes', requires=IS_NOT_EMPTY()),
                Field('user_id', 'reference auth_user', requires=IS_NOT_EMPTY()),

                )
   