from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Ton mot de passe en clair (à NE PAS stocker)
mot_de_passe = "0000"

# On hache le mot de passe
hash_mdp = bcrypt.generate_password_hash(mot_de_passe).decode('utf-8')

print("Mot de passe haché :", hash_mdp)