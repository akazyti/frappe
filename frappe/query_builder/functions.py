from pypika.functions import *

from frappe.query_builder.custom import (GROUP_CONCAT, MATCH, STRING_AGG,
                                         TO_TSVECTOR)
from frappe.query_builder.utils import ImportMapper, db_type_is

GroupConcat = ImportMapper(
	{
		db_type_is.MARIADB: GROUP_CONCAT,
		db_type_is.POSTGRES: STRING_AGG
	}
)

Match = ImportMapper(
	{
		db_type_is.MARIADB: MATCH,
		db_type_is.POSTGRES: TO_TSVECTOR
	}
)
