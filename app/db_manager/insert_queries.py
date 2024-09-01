CHARACTERS_QUERY = """
                    INSERT INTO characters (id, name, model, rank, genzone, image, has_synergy_weapon)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """

RANKS_QUERY = "INSERT INTO ranks (value, name) VALUES (?,?)"

WARP_SKILLS_QUERY = "INSERT INTO warp_skills (id, name, image, slot1, slot2) VALUES (?,?,?,?,?)"

ELEMENTS_QUERY = "INSERT INTO elements (id, name, character_id) VALUES (?,?,?)"

SIGILS_QUERY = "INSERT INTO sigils (id, name, image) VALUES (?,?,?)"

FUNCTORS_QUERY = "INSERT INTO functors (id, name, faction, rarity, main_character_id, image) VALUES (?,?,?,?,?,?)"