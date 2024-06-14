-- a SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.
DROP TRIGGER IF EXISTS decrease_quantity;
DELIMITER $$

CREATE TRIGGER decrease_quantity
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
	SET NEW.valid_email = 0;
    ELSE
    	SET NEW.valid_email = NEW.valid_email;
    END IF;
END$$

DELIMITER ;
