--3. Từ database airline lấy ra top 10 thành phố có số chuyến bay delay nhiều nhất lưu DB top10_delayed_flight_cities:
SELECT DISTINCT airport.city AS airport_city, SUM(statistics_flights.delayed) as sum_flights_delayed
  FROM airport
 INNER JOIN statistics_flights
    ON airport.product_id = statistics_flights.product_id
 GROUP BY airport_city
 ORDER BY sum_flights_delayed DESC
 LIMIT 10;
