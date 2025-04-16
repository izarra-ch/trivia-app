CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    options TEXT[] NOT NULL,
    correct_option TEXT NOT NULL
);

ALTER TABLE IF EXISTS questions OWNER TO admin;

ALTER TABLE questions ADD CONSTRAINT uq_question UNIQUE (question);

INSERT INTO questions (question, options, correct_option) VALUES
    ('¿Cuál es la capital de Francia?', ARRAY['Madrid', 'Londres', 'París', 'Berlín'], 'París'), 
    ('¿En qué país se encuentra la Torre Eiffel?', ARRAY['Italia', 'Francia', 'España', 'Alemania'], 'Francia'),
    ('¿Quién escribió ''Cien años de soledad''?', ARRAY['Mario Vargas Llosa', 'Gabriel García Márquez', 'Julio Cortázar', 'Pablo Neruda'], 'Gabriel García Márquez'), 
    ('¿Cuál es el resultado de 7 x 8?', ARRAY['54', '56', '64', '58'], '56'), 
    ('¿Cuál es el océano más grande del mundo?', ARRAY['Atlántico', 'Índico', 'Ártico', 'Pacífico'], 'Pacífico'), 
    ('¿Qué parte del cuerpo bombea la sangre?', ARRAY['Pulmones', 'Riñón', 'Hígado', 'Corazón'], 'Corazón')
ON CONFLICT (question) DO NOTHING;

SELECT setval('questions_id_seq', (SELECT MAX(id) FROM questions));