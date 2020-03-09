--2. Từ database airline lấy ra top 10 sân bay có tổng số phút bị delay nhiều nhất lưu DB
--top10_delayed_minute_airports:
SELECT airport_name, SUM(statistics_minutes_delayed_total)
    AS sum_minus_delay
  FROM data
 GROUP BY airport_name
 ORDER BY  sum_minus_delay
  DESC limit 10;