-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
CREATE TRIGGER after_email_change_update
AFTER UPDATE ON users
FOR EACH ROW
UPDATE users
SET NEW.valid_email = 0;