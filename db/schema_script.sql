-- Delete the database if it already exists (clean slate)
DROP DATABASE IF EXISTS xliff_validation;

-- Create the new database
CREATE DATABASE xliff_validation;

-- Use the newly created database
USE xliff_validation;

-- Create the validation_reports table
CREATE TABLE validation_reports (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique auto-increment ID (must be the primary key)
    file_name VARCHAR(255) NOT NULL,    -- XLIFF file name
    date_validated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Auto-filled validation date
    segment_id VARCHAR(100) NOT NULL,   -- XLIFF segment identifier
    source_text TEXT NOT NULL,          -- Original source text
    target_text TEXT NOT NULL,          -- Translated text
    qa_status VARCHAR(255) NOT NULL,    -- QA validation status (e.g., "Correct", "Mismatch/missing tag")

    -- We create a composite unique index for file_name, date_validated, and segment_id 
    UNIQUE INDEX unique_report (file_name, date_validated, segment_id), -- Ensures each segment has a unique validation entry per file/date
    
    INDEX idx_file_name (file_name),  -- Speeds up lookups by file name
    INDEX idx_date (date_validated),  -- Fast retrieval of reports by date
    INDEX idx_segment_id (segment_id) -- Efficient filtering by segment ID
);
