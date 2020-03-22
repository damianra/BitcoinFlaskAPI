# BitcoinFlaskAPI
This is a API rest in Flask Python 3.8
Database of the application have date, price and variation of Bitcoins in USD
(2010/07/18 - 2020/03/21)


# End points:
/price     -  Price in real time



/alldata   -  All data in database (2010/07/18 - 2020/03/21)



/date      -  Obtain data in especific day
Example consult:
www.domain.com/api/v1/date?date=2020/01/02
{
	"date": "2020/01/02"
}



/daterange  - Obtain data in especific date range
Example consult:
www.domain.com/api/v1/daterange?startdate=2020/01/02&enddate=2020/03/02
OR
{
	"startdate": "2020/01/02",
	"enddate": "2020/03/02"
}



/rangevariation
www.domain.com/api/v1/rangevariation?startvar=0.5&endvar=2
Example consult:
{
	"startvar": "0.5",
	"endvar": "2"
}
