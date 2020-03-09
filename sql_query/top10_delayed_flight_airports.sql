--1. Từ database airline lấy ra top 10 sân bay có số chuyến bay bị delay nhiều nhất lưu DB
--top10_delayed_flight_airports: statistics.flights.delayed.
SELECT DISTINCT airport_name, SUM(statistics_flights_delayed) as sum_flights_delayed
  FROM data
 GROUP BY airport_name
 ORDER BY sum_flights_delayed DESC
 LIMIT 10;