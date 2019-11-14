select	*
from	(select	rfid as item,
		datediff(return_timestamp, sale_timestamp) as days_between
	from	(select	rfid,
			min(case when type_detail = 'sale' then str_to_date(transaction_date_str, '%m/%e/%Y %H:%i') end) as sale_timestamp,
			max(case when type_detail = 'return' then str_to_date(transaction_date_str, '%m/%e/%Y %H:%i') end) as return_timestamp,
			count(*) as no_of_transactions
		from	transaction_detail
		group by	rfid) g1
	where	sale_timestamp is not null
	and	return_timestamp is not null
	and	no_of_transactions > 10
	group by	rfid) h1
where	days_between >= 0;