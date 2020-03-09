--5. Từ database airline lấy ra top 10 hãng có số chuyến bay delay nhiều nhất lưu DB top10_delayed_flight_carriers:

SELECT DISTINCT carrier.name AS carriers_name, SUM(statistics_flights.delayed) as sum_flights_delayed
  FROM carrier
 INNER JOIN statistics_flights
    ON carrier.id = statistics_flights.product_id
 GROUP BY carrier.name
 ORDER BY sum_flights_delayed DESC
 LIMIT 10;