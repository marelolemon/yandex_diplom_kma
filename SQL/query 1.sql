--Задание 1
--Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
--Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
SELECT "c"."login", COUNT("o"."id") as order_count
FROM "Couriers" "c"
JOIN "Orders" "o" ON "c"."id" = "o"."courierId"
WHERE "o"."inDelivery" = true
GROUP BY "c"."login";