from database.mongo import athletes_collection

def init_db():
    athletes_collection.create_index("name", unique=True)
    
    if athletes_collection.estimated_document_count() == 0:
        athletes_collection.insert_many([
            {"name": "Bruna Takahashi", "attack": 14, "defense": 16, "serve": 15},
            {"name": "Félix Lebrun", "attack": 19, "defense": 15, "serve": 18},
            {"name": "Giulia Takahashi", "attack": 13, "defense": 15, "serve": 15},
            {"name": "Hugo Calderano", "attack": 18, "defense": 17, "serve": 16},
            {"name": "Truls Möregård", "attack": 16, "defense": 15, "serve": 16},
            {"name": "Wang Chuqin", "attack": 19, "defense": 18, "serve": 19},
            {"name": "Ma Long", "attack": 20, "defense": 19, "serve": 18},
        ])