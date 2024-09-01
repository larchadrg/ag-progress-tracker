from os.path import abspath, join, dirname

BASE_DIR = dirname(abspath(__file__))

CHARACTERS_CSV_PATH = abspath(join(BASE_DIR,'csv_files','characters.csv'))
RANKS_CSV_PATH = abspath(join(BASE_DIR,'csv_files','ranks.csv'))
SIGILS_CSV_PATH = abspath(join(BASE_DIR, 'csv_files','sigils.csv'))
ELEMENTS_CSV_PATH = abspath(join(BASE_DIR,  'csv_files','elements.csv'))
WARP_SKILLS_CSV_PATH = abspath(join(BASE_DIR, 'csv_files', 'warp_skills.csv'))
