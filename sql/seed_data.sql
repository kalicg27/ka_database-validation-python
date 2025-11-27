INSERT INTO customers (email, country) VALUES
('user1@example.com', 'PL'),
('user2@example.com', 'US');

INSERT INTO products (name, price_cents) VALUES
('Sword', 1000),
('Shield', 1500);

INSERT INTO orders (customer_id) VALUES
(1),
(2);

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 2, 3);
