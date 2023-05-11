CREATE VIEW `uber-data-analytics-386214.uber_data_engineering.analytics_table` as ( 
SELECT  fct.VendorID,w.weekday, m.month,pt.payment_type_name,
        r.ratecode_name,rp.period,sff.store_and_fwd_flag_name,
        fct.passenger_count, fct.trip_distance,fct.fare_amount,
        fct.extra,fct.mta_tax,fct.tip_amount,fct.tolls_amount,
        fct.total_amount,fct.congestion_surcharge,fct.Airport_fee
FROM `uber-data-analytics-386214.uber_data_engineering.fact_table` fct
LEFT JOIN `uber-data-analytics-386214.uber_data_engineering.month` m on fct.month_id=m.month_id
LEFT JOIN `uber-data-analytics-386214.uber_data_engineering.payment_type` pt on fct.payment_type_id=pt.payment_type_id
LEFT JOIN `uber-data-analytics-386214.uber_data_engineering.ratecode` r on fct.ratecode_id=r.ratecode_id
LEFT JOIN `uber-data-analytics-386214.uber_data_engineering.ride_period` rp on fct.period_id=rp.period_id
LEFT JOIN `uber-data-analytics-386214.uber_data_engineering.store_and_fwd_flag` sff on fct.store_and_fwd_flag_id=sff.store_and_fwd_flag_id
LEFT JOIN `uber-data-analytics-386214.uber_data_engineering.weekday` w on fct.weekday_id=w.weekday_id)

select * from `uber-data-analytics-386214.uber_data_engineering.analytics_table` 