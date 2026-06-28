def get_hotels(destination):

    hotels = {
        "coimbatore":[
            {
                "name":"Vivanta Coimbatore",
                "price":"₹6500 / night",
                "rating":"4.6",
                "image":"https://images.unsplash.com/photo-1566073771259-6a8506099945"
            },
            {
                "name":"Le Meridien",
                "price":"₹5800 / night",
                "rating":"4.5",
                "image":"https://images.unsplash.com/photo-1445019980597-93fa8acb246c"
            }
        ],

        "paris":[
            {
                "name":"Hotel Eiffel",
                "price":"₹18000 / night",
                "rating":"4.8",
                "image":"https://images.unsplash.com/photo-1522708323590-d24dbb6b0267"
            },
            {
                "name":"Novotel Paris",
                "price":"₹14000 / night",
                "rating":"4.6",
                "image":"https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"
            }
        ]
    }

    return hotels.get(destination.lower(), [])