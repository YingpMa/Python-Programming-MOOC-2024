# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating = 0
        self.count = 0
        self.ave_points = 0

    def rate(self, rating: int):
        self.count += 1
        self.rating += rating
        self.ave_points = self.rating / self.count

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.rating == 0 and self.count == 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{self.count} ratings, average {self.ave_points:.1f} points"

def minimum_grade(rating: float, series_list: list):
    minimum_grade_series = []
    for item in series_list:
        if item.ave_points >= rating:
            minimum_grade_series.append(item)
    return minimum_grade_series

def includes_genre(genre: str, series_list: list):
    includes_genre = []
    for item in series_list:
        if genre in item.genres:
            includes_genre.append(item)

    return includes_genre


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    series = [s1, s2, s3]

    vastaus = minimum_grade(1.5, series)
