-- a SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.
DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
