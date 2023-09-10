
DROP TABLE pets;

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT, 
    age INTEGER,
    notes TEXT, 
    available BOOLEAN DEFAULT true
);

INSERT INTO pets (
    id,
    name,
    species,
    photo_url
)
VALUES (
    1,
    'Milo',
    'Dog',
    'https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcRWWl0PO7qFWCsi9Wvf57JmYbfLEWqWWx1mBqinse1nEvEnyomeU-Uuq_3snC1fh_nr50svczyRaZbOvBk'
);