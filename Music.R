#For reading and writes CSV and other text files.
library(readr)
#For processing and manipulating data.
library(dplyr)
music_df <- read.csv("https://query.data.world/s/i4lprljtdl664va3bm6dnbxwiu4ngd", header=TRUE, stringsAsFactors=FALSE)


rock_chart <- music_df %>%
  filter(Genre == "Rock" & Number >= 1) %>%
  arrange(desc(Number))

# Here what I'm doing is filtering all the Rock Genre music (if 'rock' is pertained in the Genre string)
# by Number (ranking), Year (Release), Artist (Name), and Album (Name)
# Limits: Weird strings such as "Soundtrack,<ca>Disco"
rock_chart2 <- music_df %>%
  filter(grepl("Rock", Genre)) %>%
  arrange(Number, Year, Artist, Album)

# Me trying to figure out which decade is the best based off music
# First i"m finding all the music created in each decade
# Next, I'm adding in categories such as Number(ranking), Album, and Genre. 
# Year is included due to my filtering, and subgenre is included I guess because of Genre
sixtys <- music_df %>%
  filter((Year >= 1960 & Year < 1970) & Number >= 1) %>%
  arrange(Number, Artist, Album)

top_sixtys <- music_df %>%
  filter((Year >= 1960 & Year < 1970) & Number >= 1) %>%
  arrange(Number, Artist, Album) %>%
  head(10)

seventies <- music_df %>%
  filter((Year >= 1970 & Year < 1980) & Number >= 1) %>%
  arrange(Number, Artist, Album)

top_seventies <- music_df %>%
  filter((Year >= 1970 & Year < 1980) & Number >= 1) %>%
  arrange(Number, Artist, Album) %>%
  head(10)

eighties <- music_df %>%
  filter((Year >= 1980 & Year < 1990) & Number >= 1) %>%
  arrange(Number, Artist, Album)

top_eighties <- music_df %>%
  filter((Year >= 1980 & Year < 1990) & Number >= 1) %>%
  arrange(Number, Artist, Album) %>%
  head(10)

nineties <- music_df %>%
  filter((Year >= 1990 & Year < 2000) & Number >= 1) %>%
  arrange(Number, Artist, Album)

top_nineties <- music_df %>%
  filter((Year >= 1990 & Year < 2000) & Number >= 1) %>%
  arrange(Number, Artist, Album) %>%
  head(10)

two_thous <- music_df %>%
  filter((Year >= 2000) & Number >= 1) %>%
  arrange(Number, Artist, Album)

top_two_thou <- music_df %>%
  filter((Year >= 2000) & Number >= 1) %>%
  arrange(Number, Artist, Album) %>%
  head(10)






