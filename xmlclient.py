# url = 'localhost'
# db = 'test_db'
# username = 'admin'
# password = 'admin'
#
# import xmlprc.client
#
# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
# version = common.version()
# print("details...", version)
#
# uid = common.authenticate(db, username, password, {})
# print("UID", uid)
#
# models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
# models.execute_kw(db, uid, password,
#     'res.partner', 'search',
#     [[['customer', '=', True]]], {'offset': 10, 'limit': 10})
# print("partners...", partners_ids)
#
# partners_count = models.execute_kw(db, uid, password,
#     'res.partner', 'search_count', [[]])
# print("partners_count...", partners_count)
#
# partner_rec = models.execute_kw(db, uid, password,
#     'res.partner', 'read', [partners_ids], {'fields': {'id', 'name'}})
# print("partner_rec....", partner_rec)
# for partner in partner_rec:
#     print(partner)
#
# abcd = models.execute_kw(db, uid, password,
#     'res.partner', 'search_read',
#     [[]], {'fields': ['id', 'name'], 'limit': 5})
# print("Search Read Results", abcd)
# for ab in abcd:
#     print(ab)
#
# new_contact = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
#     'name': "New Partner", 'mobile': "1234"
# }])
# print("Newly Created ID is", new_contact)
