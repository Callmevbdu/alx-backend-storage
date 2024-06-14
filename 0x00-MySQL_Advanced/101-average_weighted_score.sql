-- a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes and store the average
-- weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    ALTER TABLE students ADD total_weighted_marks INT NOT NULL;
    ALTER TABLE students ADD total_weights INT NOT NULL;

    UPDATE students
        SET total_weighted_marks = (
            SELECT SUM(grades.score * assignments.weight)
            FROM grades
                INNER JOIN assignments
                    ON grades.project_id = assignments.id
            WHERE grades.student_id = students.id
            );

    UPDATE students
        SET total_weights = (
            SELECT SUM(assignments.weight)
                FROM grades
                    INNER JOIN assignments
                        ON grades.project_id = assignments.id
                WHERE grades.student_id = students.id
            );

    UPDATE students
        SET students.average_marks = IF(students.total_weights = 0, 0, students.total_weighted_marks / students.total_weights);
    ALTER TABLE students
        DROP COLUMN total_weighted_marks;
    ALTER TABLE students
        DROP COLUMN total_weights;
END $$
DELIMITER ;
