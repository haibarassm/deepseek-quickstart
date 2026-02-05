-- 创建数据库
CREATE DATABASE cat_shop_simple;
\c cat_shop_simple;

-- 1. 猫猫品种表（核心表）
CREATE TABLE cat_breeds (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(50) NOT NULL,
    origin_country VARCHAR(50),
    fur_type VARCHAR(20) NOT NULL,
    personality_tags TEXT[],
    avg_weight_kg NUMERIC(4,2),
    life_expectancy_years INT,
    price_range_low INT,
    price_range_high INT,
    rarity_level VARCHAR(20) CHECK (rarity_level IN ('常见', '稀有', '非常稀有')),
    suitable_for TEXT[], -- 适合的人群
    maintenance_level VARCHAR(20) -- 养护难度
);

-- 2. 猫猫库存表（简化的库存信息）
CREATE TABLE cat_inventory (
    cat_id VARCHAR(20) PRIMARY KEY,
    breed_id INT REFERENCES cat_breeds(breed_id),
    cat_name VARCHAR(100),
    gender CHAR(1) CHECK (gender IN ('M', 'F')),
    age_months INT,
    color VARCHAR(100),
    price NUMERIC(10,2) NOT NULL,
    stock_status VARCHAR(20) DEFAULT '在售' CHECK (stock_status IN ('在售', '已预定', '已售出')),
    health_guarantee_days INT DEFAULT 7,
    description TEXT
);

-- 创建索引
CREATE INDEX idx_cat_breeds_category ON cat_breeds(category);
CREATE INDEX idx_cat_breeds_rarity ON cat_breeds(rarity_level);
CREATE INDEX idx_cat_inventory_breed ON cat_inventory(breed_id);
CREATE INDEX idx_cat_inventory_status ON cat_inventory(stock_status);