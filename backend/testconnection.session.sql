-- @block 
CREATE TABLE Clothes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(15),
    size VARCHAR(3),
    color VARCHAR(255),
    thrifted TINYINT(1) DEFAULT 0, /* boolean, where 0 = false */
    image_url VARCHAR(255)
);


-- @block
DROP TABLE Clothes;

-- @block
INSERT INTO Clothes (id, name, type, size, color, thrifted, image_url)
VALUES
(1, 'A', 'Shirt', 'S', 'red', 0, "https://m.media-amazon.com/images/I/B19qdR75OtS._CLa%7C2140%2C2000%7C61EX9VJbziL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX679_.png"), 
(2, 'B', 'Pants', 'M', 'pink', 0, "https://is4.fwrdassets.com/images/p/fw/z/BOTT-MP25_V1.jpg"), 
(3, 'C', 'Hat', 'L', 'brown', 0, "https://m.media-amazon.com/images/I/61e76Sqpg3L._AC_SX679_.jpg");

-- @block
SELECT * FROM Clothes;