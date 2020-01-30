# Data integration

istole offers out of the box integration through our API. Currently, the admin API supports:

- /get [GET]

Gets _all_ of the data from our database. This is usually used when you want to use store the data on your own, and pursue any further analysis.

```json
[
  {
    "result": [
      {
        "id": 1,
        "description": "short description",
        "long_description": "long_description",
        "lat": geographical_latitude_data,
        "long": geographical_longitude_data
      }
    ]
  }
]
```

- /get/:id [GET]

The `id` is the item ID (duh!). You can use this to get more info about a particular entity.

```json
{
  "id": 1,
  "description": "short description",
  "long_description": "long_description",
  "lat": geographical_latitude_data,
  "long": geographical_longitude_data
}
```

The api is really just that!

## iStole web app

iStole can be used as a mobile web application. This comes in very handy, as the web _is a universal runtime that is supported by all smart phones, be it iOS, or any android device_. This power feature that the web offers for us will allow for a rapid development, while we focus on other parts of the system--awareness.

## Awareness

We believe that this system can only succinctly work when awareness is in place. That's why we made Faris Character. Our friendly Sudani character whom will be used in our marketing campaign to encourage people to call for any fraud cases!

![coop figure](figure_coop.jpg)

This is a suggested figure, but we will develop a new revolutionary face figure to represent and lead this initiative.

## Dashboard

Our admin dashboard will be provided by iStole. It currently only provides geospatial data -- and more data and analysis can be provided as well.

## Android App

An android app will be developed to used throughout the system. It will support the main web app.

## iOS App

An iOS app will be developed to used throughout the system. It will support the main web app.
