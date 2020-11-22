#For reading and writes CSV and other text files.
library(readr)
#For processing and manipulating data.
library(dplyr)
# load packages to read, write and manipulate data
#pfizer <- read_csv("pfizer.csv")
#fda <- read_csv("fda.csv")

# view structure of data
str(pfizer)
str(fda)

# convert total to numeric variable
pfizer$total <- as.numeric(pfizer$total)
str(pfizer)

# summary of pfizer data
summary(pfizer)

# doctors in California who were paid $10,000 or more by Pfizer to run “Expert-Led Forums.”
ca_paid_doctors <- pfizer %>%
  filter(state == "CA" & total >= 10000 & category == "Expert-Led Forums") %>%
  arrange(desc(total))

ca_ny_paid_doctors <- pfizer %>%
  filter((state == "CA" | state == "NY") & total >= 10000 & category == "Expert-Led Forums") %>%
  arrange(desc(total))

# Find the 20 doctors across the four largest states (CA, TX, FL, NY) who were paid the most for professional advice.
ca_ny_tx_fl_prof_top20 <- pfizer %>%
  filter((state=="CA" | state == "NY" | state == "TX" | state == "FL") & category == "Professional Advising") %>%
  arrange(desc(total)) %>%
  head(20)

# Filter the data for all payments for running Expert-Led Forums or for Professional Advising, and arrange alphabetically by doctor (last name, then first name
# expert_advice <- pfizer %>%
  # filter(category == "Expert-Led Forums" | category == "Professional Advising") %>%
  # arrange(last_name, first_name)


# use pattern matching to filter text
expert_advice <- pfizer %>%
  filter(grepl("Expert|Professional", category)) %>%
  arrange(last_name, first_name)

not_expert_advice <- pfizer %>%
  filter(!grepl("Expert|Professional", category)) %>%
  arrange(last_name, first_name)


# merge/append data frames
pfizer2 <- bind_rows(expert_advice, not_expert_advice)
# write expert_advice data to a csv file
write_csv(expert_advice, "expert_advice.csv", na="")

# Ranking the net total earned by state
state_sum <- pfizer %>%
  group_by(state) %>%
  summarize(sum = sum(total)) %>%
  arrange(desc(sum))

# Ranking the net total earned by city
city_sum <- pfizer %>%
  group_by(city) %>%
  summarize(sum = sum(total)) %>%
  arrange(desc(sum))

# Ranking the net total earned by category
cat_sum <- pfizer %>%
  group_by(category) %>%
  summarize(sum = sum(total)) %>%
  arrange(desc(sum))

# Ranking the net total earned by doctor name, included city and state
doc_sum <- pfizer %>%
  group_by(last_name, first_name, city, state) %>%
  summarize(sum = sum(total)) %>%
  arrange(desc(sum))

letters_year <- fda %>%
  mutate(year = format(issued, "%Y")) %>%
  group_by(name_last, name_first) %>%
  summarize(letters=n())


# join to identify doctors paid over $1,000 who also received a warning letter
expert_warned2 <- inner_join(pfizer, fda, by=c("first_name" = "name_first", "last_name" = "name_last")) %>%
  filter(total>= 1000) %>%
  select(first_name, last_name, city, state, total, issued)

# join to compare the doctors paid over $1,000 who also received a warning letter
# Based on comparing data with doc_sum
not_warned <- inner_join(doc_sum, fda, by=c("first_name" = "name_first", "last_name" = "name_last")) %>%
  filter(sum >= 1000) %>%
  select(first_name, last_name, city, state, sum)

# References:
# Code above from "https://paldhous.github.io/ucb/2016/dataviz/week7.html"
# Altered by me for pure curiosity purposes


