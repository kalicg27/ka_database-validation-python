CREATE TABLE customers (
    id           SERIAL PRIMARY KEY,
    email        VARCHAR(255) NOT NULL UNIQUE,
    country      VARCHAR(2)   NOT NULL,
    created_at   TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE products (
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(255) NOT NULL,
    price_cents  INTEGER      NOT NULL CHECK (price_cents > 0)
);

CREATE TABLE orders (
    id           SERIAL PRIMARY KEY,
    customer_id  INTEGER      NOT NULL REFERENCES customers(id),
    created_at   TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE order_items (
    id           SERIAL PRIMARY KEY,
    order_id     INTEGER      NOT NULL REFERENCES orders(id),
    product_id   INTEGER      NOT NULL REFERENCES products(id),
    quantity     INTEGER      NOT NULL CHECK (quantity > 0)
);
