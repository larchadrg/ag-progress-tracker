DROP TABLE IF EXISTS characters; 
DROP TABLE IF EXISTS elements; 
DROP TABLE IF EXISTS ranks; 
DROP TABLE IF EXISTS sigils; 
DROP TABLE IF EXISTS warp_skills; 


CREATE TABLE sigils (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                image TEXT NOT NULL
                );
CREATE TABLE ranks (
                value TEXT PRIMARY KEY,
                name TEXT NOT NULL
                );
CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY,
                name TEXT,
                model TEXT,
                rank TEXT,
                genzone TEXT,
                image TEXT,
                has_synergy_weapon BOOLEAN DEFAULT 0, 
                FOREIGN KEY (rank) REFERENCES ranks(value)
                );
CREATE TABLE IF NOT EXISTS warp_skills (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                image TEXT,
                slot1 INTEGER NOT NULL,
                slot2 INTEGER NOT NULL
                );
CREATE TABLE IF NOT EXISTS elements(
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "character_id" INTEGER NOT NULL,
    FOREIGN KEY("character_id") REFERENCES "characters"("id")
);