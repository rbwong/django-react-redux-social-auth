# Django + React/Redux + Social Authentication Base Project (Ongoing Project)

I decided to create this project to incorporate Social Authentication in [Django React/Redux Base Project](https://github.com/Seedstars/django-react-redux-jwt-base)

The project was built with the following technologies:

**Frontend**

* [React](https://github.com/facebook/react)
* [React Router](https://github.com/rackt/react-router)
* [JSON Web Token](https://www.npmjs.com/package/jsonwebtoken) JSON Web Token for API authentication
* [Babel](http://babeljs.io) for ES6 and ES7 magic
* [Webpack](http://webpack.github.io) for bundling
* [Webpack Dev Middleware](http://webpack.github.io/docs/webpack-dev-middleware.html)
* [Redux](https://github.com/rackt/redux)'s futuristic [Flux](https://facebook.github.io/react/blog/2014/05/06/flux.html) implementation
* [Redux Dev Tools](https://github.com/rackt/redux-devtools) for next generation DX (developer experience). Watch [Dan Abramov's talk](https://www.youtube.com/watch?v=xsSnOQynTHs)
* [Redux Thunk](https://github.com/gaearon/redux-thunk) Thunk middleware for Redux - used in async actions
* [React Router Redux](https://github.com/rackt/react-router-redux) Ruthlessly simple bindings to keep react-router and redux in sync
* [fetch](https://github.com/github/fetch) A window.fetch JavaScript polyfill
* [style-loader](https://github.com/webpack/style-loader), [sass-loader](https://github.com/jtangelder/sass-loader) and [less-loader](https://github.com/webpack/less-loader) to allow import of stylesheets in plain css, sass and less,
* [bootstrap-sass-loader](https://github.com/shakacode/bootstrap-sass-loader) and [font-awesome-webpack](https://github.com/gowravshekar/font-awesome-webpack) to customize Bootstrap and FontAwesome
* [ESLint](http://eslint.org), [Airbnb Javascript/React Styleguide](https://github.com/airbnb/javascript), [Airbnb CSS / Sass Styleguide](https://github.com/airbnb/css) to maintain a consistent code style and [eslint-plugin-import](https://github.com/benmosher/eslint-plugin-import) to make sure all imports are correct
* [mocha](https://mochajs.org/) to allow writing unit tests for the project
* [redux-mock-store](https://github.com/arnaudbenard/redux-mock-store) a mock store for your testing your redux async action creators and middleware
* [expect](https://github.com/mjackson/expect) Write better assertions
* [Nock](https://github.com/pgte/nock) HTTP mocking and expectations library
* [istanbul](https://github.com/gotwarlost/istanbul) to generate coverage when running mocha

**Backend**

* [Django](https://www.djangoproject.com/)
* [Django REST framework](http://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs
* [Django REST Auth](https://github.com/Tivix/django-rest-auth) for Authtentication
* [Django All Auth](http://django-allauth.readthedocs.org/) for Social Authtentication
* [WhiteNoise](http://whitenoise.evans.io/en/latest/django.html) to serve files efficiently from Django
* [Responses](https://github.com/getsentry/responses) a utility for mocking out the Python Requests library



## Retrieve code 

* `$ git clone https://github.com/Seedstars/django-react-redux-base.git`
* `$ cd django-react-redux-jwt-base`
* `$ git submodule init`
* `$ git submodule update`
* `$ ./scripts/get_static_validation.sh`

Remember that when you copy this repository for a new project you need to add the scripts external module using:

* `$ git submodule add https://github.com/Seedstars/culture-scripts scripts`

## Installation

* `$ npm install`
* `$ npm run dev`

* `$ pip install -r py-requirements/dev.txt`

* `$ cd src`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

## Post-Installation
Now start your server, visit your admin pages (e.g. http://localhost:8000/admin/) and follow these steps:

1. Add a Site for your domain, matching settings.SITE_ID (django.contrib.sites app).

2. For each OAuth based provider, add a Social App (socialaccount app).

3. Fill in the site and the OAuth app credentials obtained from the provider.

## Running

Run webpack in development mode

* `$ npm run dev` 

Run Django development http server 

* `$ cd src`
* `$ python manage.py runserver`