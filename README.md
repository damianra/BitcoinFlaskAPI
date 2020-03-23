# BitcoinFlaskAPI
This is a API rest in Flask Python 3.8
Database of the application have date, price and variation of Bitcoins in USD
(2010/07/18 - 2020/03/21)


# End points:
/api/v1/price     -  Price in real time


/api/v1/alldata   -  All data in database (2010/07/18 - 2020/03/21)


/api/v1/date      -  Obtain data in especific day</br>
Example consult:</br>
www.domain.com/api/v1/date?date=2020/01/02</br>
{</br>
	"date": "2020/01/02"</br>
}</br>
</br>


/api/v1/daterange  - Obtain data in especific date range</br>
Example consult:</br>
www.domain.com/api/v1/daterange?startdate=2020/01/02&enddate=2020/03/02</br></br>
OR</br></br>
{</br>
	"startdate": "2020/01/02",</br>
	"enddate": "2020/03/02"</br>
}</br>

</br>

/api/v1/rangevariation</br>
www.domain.com/api/v1/rangevariation?startvar=0.5&endvar=2</br></br>
OR</br></br>
Example consult:</br>
{</br>
	"startvar": "0.5",</br>
	"endvar": "2"</br>
}</br>
