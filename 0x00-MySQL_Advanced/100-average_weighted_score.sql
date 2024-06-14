-- a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and store the average
-- weighted score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight FLOAT;
    DECLARE total_score FLOAT;

    -- Compute the total weight
    SELECT SUM(weight) INTO total_weight
    FROM projects
    INNER JOIN corrections ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;

    -- Compute the total score
    SELECT SUM(score * weight) INTO total_score
    FROM projects
    INNER JOIN corrections ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;

    -- Update the average score in the users table
    UPDATE users SET average_score = total_score / total_weight WHERE id = user_id;
END$$

DELIMITER ;
