import pandas as pd

# Popüler ve zengin film veri seti (Aksiyon, Bilim Kurgu, Dram, Macera, Animasyon vb.)
movies_data = [
    {
        "id": 1,
        "title": "Inception (Başlangıç)",
        "genres": "Aksiyon Bilim Kurgu Gerilim",
        "director": "Christopher Nolan",
        "cast": "Leonardo DiCaprio Joseph Gordon-Levitt Elliot Page",
        "overview": "Rüya paylaşımı teknolojisi ile insanların zihnine girip sırları çalan bir hırsıza, bir CEO'nun zihnine fikir ekleme görevi verilir.",
    },
    {
        "id": 2,
        "title": "Interstellar (Yıldızlararası)",
        "genres": "Macera Dram Bilim Kurgu",
        "director": "Christopher Nolan",
        "cast": "Matthew McConaughey Anne Hathaway Jessica Chastain",
        "overview": "Dünya yaşanmaz hale geldiğinde, eski bir NASA pilotu insanlık için yeni bir yaşanabilir gezegen bulmak üzere uzay yolculuğuna çıkar.",
    },
    {
        "id": 3,
        "title": "The Dark Knight (Kara Şövalye)",
        "genres": "Aksiyon Suç Dram Gerilim",
        "director": "Christopher Nolan",
        "cast": "Christian Bale Heath Ledger Aaron Eckhart",
        "overview": "Gotham sokaklarında kaos yaratan Joker ortaya çıktığında, Batman adalet için en büyük psikolojik sınavını verir.",
    },
    {
        "id": 4,
        "title": "The Matrix",
        "genres": "Aksiyon Bilim Kurgu",
        "director": "Lana Wachowski Lilly Wachowski",
        "cast": "Keanu Reeves Laurence Fishburne Carrie-Anne Moss",
        "overview": "Bir bilgisayar korsanı, yaşadığı dünyanın yapay bir zeka tarafından kontrol edilen bir simülasyon olduğunu öğrenir ve isyana katılır.",
    },
    {
        "id": 5,
        "title": "Avatar",
        "genres": "Aksiyon Macera Fantastik Bilim Kurgu",
        "director": "James Cameron",
        "cast": "Sam Worthington Zoe Saldana Sigourney Weaver",
        "overview": "Pandora gezegenine gönderilen felçli bir deniz piyadesi, emirleri yerine getirmek ile evi gibi hissettiği halkı korumak arasında kalır.",
    },
    {
        "id": 6,
        "title": "Titanic",
        "genres": "Dram Romantik",
        "director": "James Cameron",
        "cast": "Leonardo DiCaprio Kate Winslet Billy Zane",
        "overview": "Lüks ve talihsiz Titanic gemisinde, zengin bir genç kadın ile fakir bir ressam arasında efsanevi bir aşk doğar.",
    },
    {
        "id": 7,
        "title": "Spider-Man (Örümcek Adam)",
        "genres": "Aksiyon Macera Bilim Kurgu",
        "director": "Sam Raimi",
        "cast": "Tobey Maguire Willem Dafoe Kirsten Dunst",
        "overview": "Genetik olarak değiştirilmiş bir örümcek tarafından ısırılan Peter Parker, süper güçler kazanır ve şehri kötülüklerden korumaya başlar.",
    },
    {
        "id": 8,
        "title": "Spider-Man 2",
        "genres": "Aksiyon Macera Bilim Kurgu",
        "director": "Sam Raimi",
        "cast": "Tobey Maguire Alfred Molina Kirsten Dunst",
        "overview": "Peter Parker, Doktor Ahtapot'a karşı savaşırken bir yandan da sivil hayatı ile süper kahraman kimliği arasındaki dengeyi kurmaya çalışır.",
    },
    {
        "id": 9,
        "title": "The Avengers (Yenilmezler)",
        "genres": "Aksiyon Bilim Kurgu Macera",
        "director": "Joss Whedon",
        "cast": "Robert Downey Jr. Chris Evans Scarlett Johansson",
        "overview": "Dünyanın en güçlü süper kahramanları, dünyayı istila etmeye çalışan uzaylı ordusunu durdurmak için bir araya gelir.",
    },
    {
        "id": 10,
        "title": "Iron Man (Demir Adam)",
        "genres": "Aksiyon Macera Bilim Kurgu",
        "director": "Jon Favreau",
        "cast": "Robert Downey Jr. Gwyneth Paltrow Terrence Howard",
        "overview": "Milyarder mühendis Tony Stark, fidyecilerin elinden kurtulmak için yüksek teknolojili zırhlı bir giysi icat eder.",
    },
    {
        "id": 11,
        "title": "Harry Potter and the Philosopher's Stone",
        "genres": "Macera Fantastik Aile",
        "director": "Chris Columbus",
        "cast": "Daniel Radcliffe Emma Watson Rupert Grint",
        "overview": "Yetim bir çocuk 11. yaş gününde büyücü olduğunu öğrenir ve Hogwarts Cadılık ve Büyücülük Okulu'na kabul edilir.",
    },
    {
        "id": 12,
        "title": "Harry Potter and the Chamber of Secrets",
        "genres": "Macera Fantastik Gizem",
        "director": "Chris Columbus",
        "cast": "Daniel Radcliffe Emma Watson Rupert Grint",
        "overview": "Harry Potter, Hogwarts'taki ikinci yılında okuldaki öğrencileri taşa çeviren gizemli Sırlar Odası'nın peşine düşer.",
    },
    {
        "id": 13,
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "genres": "Aksiyon Macera Fantastik",
        "director": "Peter Jackson",
        "cast": "Elijah Wood Ian McKellen Viggo Mortensen",
        "overview": "Genç bir Hobbit, dünyayı yok edebilecek güce sahip Tek Yüzük'ü yok etmek için zorlu bir yolculuğa çıkar.",
    },
    {
        "id": 14,
        "title": "The Lord of the Rings: The Return of the King",
        "genres": "Aksiyon Macera Dram Fantastik",
        "director": "Peter Jackson",
        "cast": "Elijah Wood Ian McKellen Viggo Mortensen",
        "overview": "Orta Dünya'nın kaderi belirlenirken Sauron'un ordularına karşı son ve büyük bir savaş verilir.",
    },
    {
        "id": 15,
        "title": "Fight Club (Dövüş Kulübü)",
        "genres": "Dram Gerilim",
        "director": "David Fincher",
        "cast": "Brad Pitt Edward Norton Helena Bonham Carter",
        "overview": "Uykusuzluk çeken bir ofis çalışanı ile karizmatik bir sabun satıcısının kurduğu gizli dövüş kulübü beklenmedik bir harekete dönüşür.",
    },
    {
        "id": 16,
        "title": "Shutter Island (Zindan Adası)",
        "genres": "Gizem Gerilim Dram",
        "director": "Martin Scorsese",
        "cast": "Leonardo DiCaprio Mark Ruffalo Ben Kingsley",
        "overview": "Bir federal ajan, akıl hastalarının bulunduğu izole bir ada hastanesinden kaçan bir katilin peşine düşer.",
    },
    {
        "id": 17,
        "title": "Pulp Fiction (Ucuz Roman)",
        "genres": "Suç Dram",
        "director": "Quentin Tarantino",
        "cast": "John Travolta Uma Thurman Samuel L. Jackson",
        "overview": "İki mafya tetikçisi, bir boksör ve bir gangsterin eşinin yollarının kesiştiği kara mizah dolu hikayeler.",
    },
    {
        "id": 18,
        "title": "The Wolf of Wall Street (Para Avcısı)",
        "genres": "Biyografi Komedi Suç",
        "director": "Martin Scorsese",
        "cast": "Leonardo DiCaprio Jonah Hill Margot Robbie",
        "overview": "Borsada hızlı yoldan zengin olan Jordan Belfort'un lüks, para ve dolandırıcılıkla dolu yükselişi ve düşüşü.",
    },
    {
        "id": 19,
        "title": "Gladiator (Gladyatör)",
        "genres": "Aksiyon Macera Dram",
        "director": "Ridley Scott",
        "cast": "Russell Crowe Joaquin Phoenix Connie Nielsen",
        "overview": "Ailesi katledilen ve köle yapılan Romalı general Maximus, intikam almak için arenada bir gladyatör olarak yükselir.",
    },
    {
        "id": 20,
        "title": "La La Land (Aşıklar Şehri)",
        "genres": "Komedi Dram Müzikal Romantik",
        "director": "Damien Chazelle",
        "cast": "Ryan Gosling Emma Stone Rosemarie DeWitt",
        "overview": "Los Angeles'ta kariyer yapmaya çalışan bir caz piyanisti ile oyuncu bir kadının tutkulu aşkı ve hayalleri arasındaki çatışma.",
    },
    {
        "id": 21,
        "title": "The Notebook (Not Defteri)",
        "genres": "Dram Romantik",
        "director": "Nick Cassavetes",
        "cast": "Ryan Gosling Rachel McAdams James Garner",
        "overview": "Sosyal sınıf farklılıkları yüzünden ayrılan ama birbirini asla unutamayan iki gencin yıllara yayılan aşk hikayesi.",
    },
]


def create_dataset():
    df = pd.DataFrame(movies_data)
    df.to_csv("movies.csv", index=False)
    print("✅ Film veri seti oluşturuldu ve 'movies.csv' olarak kaydedildi!")
    print(f"Toplam Film Sayısı: {len(df)}")


if __name__ == "__main__":
    create_dataset()