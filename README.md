# scrape-n-download-google-images
It is an application that scrapes and dowloads Google Images with Python.

### Project Setup
```sh
pip install requests bs4
```
```sh
mkdir Scraped_Images
```

### Run
```sh
python index.py
```

### Test Inputs
queryParameters = {"q": "marvel", "tbm": "isch", "hl": "en", "gl": "us", "ijn": "0" }

### Output
<img width="791" alt="image" src="https://user-images.githubusercontent.com/47754791/202731530-87589ca3-f64c-4bc0-94c3-0a92b1bd7344.png">

```sh
[
  {
    'image_title': 'Marvel Comics - Wikipedia',
    'image_source_link': 'https://en.wikipedia.org/wiki/Marvel_Comics',
    'image_link': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Marvel_Logo.svg/1200px-Marvel_Logo.svg.png'
  },
  {
    'image_title': 'Marvel Universe - Wikipedia',
    'image_source_link': 'https://en.wikipedia.org/wiki/Marvel_Universe',
    'image_link': 'https://upload.wikimedia.org/wikipedia/en/1/19/Marvel_Universe_%28Civil_War%29.jpg'
  },
  {
    'image_title': 'Marvel.com | The Official Site for Marvel Movies, Characters, Comics, TV',
    'image_source_link': 'https://www.marvel.com/',
    'image_link': 'https://i.annihil.us/u/prod/marvel/images/OpenGraph-TW-1200x630.jpg'
  },
  {
    'image_title': 'Marvel Entertainment - YouTube',
    'image_source_link': 'https://www.youtube.com/c/marvel',
    'image_link': 'https://yt3.ggpht.com/fGvQjp1vAT1R4bAKTFLaSbdsfdYFDwAzVjeRVQeikH22bvHWsGULZdwIkpZXktcXZc5gFJuA3w=s900-c-k-c0x00ffffff-no-rj'
  },
  {
    'image_title': 'Marvel movies and shows | Disney+',
    'image_source_link': 'https://www.disneyplus.com/brand/marvel',
    'image_link': 'https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/DA2E198288BFCA56AB53340211B38DE7134E40E4521EDCAFE6FFB8CD69250DE9/scale?width=2880&aspectRatio=1.78&format=jpeg'
  },
  {
    'image_title': 'An Intro to Marvel for Newbies | WIRED',
    'image_source_link': 'https://www.wired.com/2012/03/an-intro-to-marvel-for-newbies/',
    'image_link': 'https://media.wired.com/photos/5955ceabcbd9b77a41915cf6/master/pass/marvel-characters.jpg'
  },
  {
    'image_title': 'How to Watch Every Marvel Movie in Order of Story - Parade: Entertainment,  Recipes, Health, Life, Holidays',
    'image_source_link': 'https://parade.com/1009863/alexandra-hurtado/marvel-movies-order/',
    'image_link': 'https://parade.com/.image/t_share/MTkwNTgxMjkxNjk3NDQ4ODI4/marveldisney.jpg'
  },
  {
    'image_title': 'Marvel Comics | History, Characters, Facts, & Movies | Britannica',
    'image_source_link': 'https://www.britannica.com/topic/Marvel-Comics',
    'image_link': 'https://cdn.britannica.com/62/182362-050-BD31B42D/Scarlett-Johansson-Black-Widow-Chris-Hemsworth-Thor.jpg'
  },
  {
    'image_title': 'Captain Marvel (2019) - IMDb',
    'image_source_link': 'https://www.imdb.com/title/tt4154664/',
    'image_link': 'https://m.media-amazon.com/images/M/MV5BMTE0YWFmOTMtYTU2ZS00ZTIxLWE3OTEtYTNiYzBkZjViZThiXkEyXkFqcGdeQXVyODMzMzQ4OTI@._V1_FMjpg_UX1000_.jpg'
  },
  {
    'image_title': 'Earth-616 | Marvel Database | Fandom',
    'image_source_link': 'https://marvel.fandom.com/wiki/Earth-616',
    'image_link': 'https://static.wikia.nocookie.net/marveldatabase/images/e/e1/The_Marvel_Universe.png/revision/latest?cb=20110513164401'
  },
  {
    'image_title': 'Marvel Contest of Champions - Apps on Google Play',
    'image_source_link': 'https://play.google.com/store/apps/details?id=com.kabam.marvelbattle&hl=en_US&gl=US',
    'image_link': 'https://play-lh.googleusercontent.com/yTq1FcqU9NJPIVwDi73W4ygCnm0fOI3O6FG4lccosA9_zxICZ2ckEri6Mh7fLtQHbMlV'
  },
  {
    'image_title': 'Marvel Makes an Epic Return to D23 Expo with a Thrilling Lineup of Panels,  Events, First Looks, and More - D23',
    'image_source_link': 'https://d23.com/marvel-makes-an-epic-return-to-d23-expo/',
    'image_link': 'https://d23.com/app/uploads/2022/08/1180w-600h_080222_marvel-d23-expo_00.jpg'
  },
  {
    'image_title': 'Marvel Cinematic Universe - Wikipedia',
    'image_source_link': 'https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe',
    'image_link': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Marvel_Cinematic_Universe_logo.png/1200px-Marvel_Cinematic_Universe_logo.png'
  },
  {
    'image_title': 'Marvel Movies | Marvel Cinematic Universe (MCU) | Marvel Studios Films',
    'image_source_link': 'https://www.marvel.com/movies',
    'image_link': 'https://terrigen-cdn-dev.marvel.com/content/prod/1x/blackpantherwakandaforever_lob_crd_05.jpg'
  },
  {
    'image_title': 'Marvel Snap is 5D chess in six minutes or less - The Verge',
    'image_source_link': 'https://www.theverge.com/2022/10/19/23413064/marvel-snap-second-dinner-hearthstone-ios-android',
    'image_link': 'https://cdn.vox-cdn.com/thumbor/TKAUJs-X0T0IXwnEk1YJclO_49o=/0x0:1920x1080/1400x1400/filters:focal(960x540:961x541)/cdn.vox-cdn.com/uploads/chorus_asset/file/24124186/PC_DARK_KA2_HORIZ_DIGITAL_FINAL_SIMPLE_BLEED_09.22.2022.jpg'
  },
  {
    'image_title': "Marvel's Avengers on Steam",
    'image_source_link': 'https://store.steampowered.com/app/997070/Marvels_Avengers/',
    'image_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/997070/capsule_616x353.jpg?t=1661334675'
  },
  {
    'image_title': 'Marvel Studios on Twitter: "Just announced in Hall H: Marvel Studios\'  Avengers: Secret Wars, in theaters November 7, 2025. #SDCC2022  https://t.co/FXQ5ZbzQYl" / Twitter',
    'image_source_link': 'https://twitter.com/marvelstudios/status/1551009742604013568',
    'image_link': 'https://pel/i/mg/3/b0/61d4c518767b4/clean.jpg'
  },
  {
    'image_title': "The Winter Soldier Joins Marvel's Avengers Later This Month - IGN",
    'image_source_link': 'https://www.ign.com/articles/the-winter-soldier-joins-marvels-avengers-later-this-month',
    'image_link': 'https://assets1.ignimgs.com/2020/02/14/marvels-avengers---button-2020-1581705831993.jpg'
  },
  {
    'image_title': 'Marvel Boss Kevin Feige Explains Why Phase 4 Projects Are So Different',
    'image_source_link': 'https://thedirect.com/article/marvel-phase-4-kevin-feige-different',
    'image_link': 'https://images.thedirect.com/media/article_full/phase-4-mcu-marvel.jpg'
  }
]
```

