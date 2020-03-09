--6. Từ top10_delayed_flight_carriers lấy ra 10 sân bay có tổng số  phút bị delay nhiều nhất
--(mỗi sân bay ứng với 1 hãng hàng không) lưu DB top10_delayed_minute_airport_carriers

SELECT airport.name AS airport_name, top10_delayed_flight_carriers.name AS top10_delayed_flight_cities_city,
       SUM(statistics_minutes_delays.total) AS minutes_delays_total
  FROM airport
 INNER JOIN statistics_minutes_delays
    ON airport.product_id = statistics_minutes_delays.product_id
 INNER JOIN carrier
    ON carrier.id = statistics_minutes_delays.product_id
 INNER JOIN top10_delayed_flight_carriers
    ON carrier.name = top10_delayed_flight_carriers.name
 GROUP BY airport_name, top10_delayed_flight_cities_city
 ORDER BY minutes_delays_total DESC
 LIMIT 10;