#📦 Epic Games Free Games Scraper

A small Python script that fetches currently free games from the Epic
Games Store using their public promotions endpoint.
It filters games where the original price is non-zero but the discount
price is zero — meaning they are temporarily free.

------------------------------------------------------------------------

#🚀 Features

-   🔍 Fetches live data from the Epic Games Store
-   🆓 Automatically detects all currently free titles
-   📝 Prints each game’s title and description
-   🛡️ Includes basic error handling for API failures

------------------------------------------------------------------------

#🧰 Requirements

Make sure you have Python 3.8+ and install dependencies:

    pip install requests json

------------------------------------------------------------------------

#🕹️ Usage

Run the script with:

    python script.py

If free games are available, you’ll see output like:

    **Titre:** Game Name
    **Description:** Game description here
    ------------------------------------------------------------

If no games are free, the script will notify you.

------------------------------------------------------------------------

#🧪 API Used

The script calls:

    https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=FR

It extracts:

-   title
-   description
-   price.totalPrice.discountPrice
-   price.totalPrice.originalPrice

Then it filters titles that are temporarily free.

------------------------------------------------------------------------

#📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.

------------------------------------------------------------------------

#🤝 Contributing

Issues and pull requests are welcome!

------------------------------------------------------------------------

⭐ Support

If you find this useful, please consider starring the repository 😊
