--4. Từ top10_delayed_flight_cities lấy ra 10 sân bay có tổng số phút bị delay nhiều nhất (mỗi sân bay ứng với
--1 thành phố) lưu DB top10_minute_delayed_flight_cities

SELECT airport.name AS airport_name, top10_delayed_flight_cities.city AS top10_delayed_flight_cities_city,
       SUM(statistics_minutes_delays.total) AS minutes_delays_total
  FROM airport
 INNER JOIN statistics_minutes_delays
    ON airport.product_id = statistics_minutes_delays.product_id
 INNER JOIN top10_delayed_flight_cities
    ON airport.city = top10_delayed_flight_cities.city
 GROUP BY airport_name, top10_delayed_flight_cities_city
 ORDER BY minutes_delays_total DESC
 LIMIT 10;