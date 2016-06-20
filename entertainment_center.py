import fresh_tomatoes  #Generates site
import media  #Provides the class Movie to store movie related information

gladiator = media.Movie(
    "Gladiator",
    "When a Roman general is betrayed and his family murdered"
    " by an emperor's corrupt son, he comes to Rome "
    "as a gladiator to seek revenge.",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=owK1qxDselE")

patch_adams = media.Movie(
    "Patch Adams",
    "In the 1970s, a medical student treats patients,"
    " illegally, using humor.",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Patch_Adams.jpg",
    "https://www.youtube.com/watch?v=bKQdKRC2DVs")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

the_imitation_game = media.Movie(
    "The Imitation Game",
    "During World War II, mathematician Alan Turing tries to"
    "crack the enigma code with help from fellow mathematicians.",
    "http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM")

les_miserables = media.Movie(
    "Les Miserables",
    "In 19th-century France, Jean Valjean, who for decades has been hunted "
    "by the ruthless policeman Javert after breaking parole, agrees to care "
    "for a factory worker's daughter. The decision changes their lives "
    "for ever.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Les-miserables-movie-poster1.jpg",
    "https://www.youtube.com/watch?v=YmvHzCLP6ug")

a_beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "After a brilliant but asocial mathematician, John Nash,"
    " accepts secret work in cryptography, his life takes a"
    " turn for the nightmarish.",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
    "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

movies = [
    gladiator, patch_adams, school_of_rock,
    the_imitation_game, les_miserables, a_beautiful_mind]
fresh_tomatoes.open_movies_page(movies)
