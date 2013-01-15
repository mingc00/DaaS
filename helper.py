import boto

def list_all():
    sdb_domain = boto.connect_sdb().get_domain('daas')
    query = 'select * from `daas`'
    rs = sdb_domain.select(query)
    return rs

def get_url(checksum, filename):
    conn = boto.connect_s3()
    header = {'response-content-disposition': 'attachment; filename='+filename}
    return conn.generate_url(6000, method='GET', bucket='daas.shume.in',
            key=checksum,
            response_headers=header)