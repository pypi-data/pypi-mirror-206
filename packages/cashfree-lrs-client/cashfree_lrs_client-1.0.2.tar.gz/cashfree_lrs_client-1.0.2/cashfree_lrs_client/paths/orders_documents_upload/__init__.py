# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from cashfree_lrs_client.paths.orders_documents_upload import Api

from cashfree_lrs_client.paths import PathValues

path = PathValues.ORDERS_DOCUMENTS_UPLOAD