-- Trigger to ensure email validation
-- Resets 'valid_email' attribute only when the email is updated

DELIMITER $$
CREATE TRIGGER resets_valid_email BEFORE UPDATE ON users
FOR EACH ROW
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER;