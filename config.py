link = 'https://www.youtube.com/watch?v=Qa30VmcLwGg'
# link = 'https://www.youtube.com/watch?v=i44g8-FrAU8'
driver_file = './chromedriver.exe'

# Browser variables
settings_btn = '//*[@id="movie_player"]/div[26]/div[2]/div[2]/button[4]'
settings_btn_2 = '//*[@id="movie_player"]/div[29]/div[2]/div[2]/button[4]' # for videos having chapters

# in seconds
long_delay = 3 # to allow page to load
vs_delay = 0.15 # for keyboard events
watch_time = 10 

# for generating random seek taps
min_ = 1
max_ = 100

# for randomized watch_time duration (in seconds)
min_wt = 60
max_wt = 600